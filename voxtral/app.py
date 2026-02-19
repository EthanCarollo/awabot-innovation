"""
Voxtral Realtime — Prototype Caméra + Transcription
====================================================
App Gradio qui affiche :
  • un retour webcam en direct
  • la transcription audio temps-réel via Voxtral (vLLM Realtime API)

Prérequis :
  1. Lancer vLLM : bash serve.sh
  2. Lancer cette app : python app.py --host localhost --port 8000

L'audio du micro est streamé via websocket vers le serveur vLLM qui renvoie
la transcription en delta. Le texte est affiché par-dessus le flux vidéo.
"""

import argparse
import asyncio
import base64
import json
import queue
import threading
import time

import cv2
import gradio as gr
import numpy as np
import websockets

# ── Configuration ────────────────────────────────────────────────
SAMPLE_RATE = 16_000
MAX_TRANSCRIPT_LINES = 6   # Nombre de lignes affichées sur la vidéo
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
FONT_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)
FONT_THICKNESS = 2

# ── État global ──────────────────────────────────────────────────
audio_queue: queue.Queue = queue.Queue()
transcription_text = ""
is_running = False
ws_url = ""
model_name = ""

# ── Webcam ───────────────────────────────────────────────────────
cap = None


def open_camera(device: int = 0) -> cv2.VideoCapture:
    """Ouvrir la caméra avec un fallback."""
    c = cv2.VideoCapture(device)
    if not c.isOpened():
        raise RuntimeError(f"Impossible d'ouvrir la caméra (device={device})")
    c.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    c.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    return c


def grab_frame_with_overlay() -> np.ndarray | None:
    """Capturer une frame et y superposer la transcription."""
    global cap
    if cap is None or not cap.isOpened():
        return None
    ret, frame = cap.read()
    if not ret:
        return None

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Récupérer les dernières lignes de transcription
    text = transcription_text.strip()
    if text:
        lines = text.split("\n")
        # Garder les dernières lignes, couper les lignes trop longues
        display_lines = []
        for line in lines:
            # Wrap lines at ~80 chars
            while len(line) > 80:
                display_lines.append(line[:80])
                line = line[80:]
            if line:
                display_lines.append(line)
        display_lines = display_lines[-MAX_TRANSCRIPT_LINES:]

        h, w = frame.shape[:2]
        line_height = 30
        padding = 10
        overlay_h = len(display_lines) * line_height + 2 * padding
        overlay_y = h - overlay_h - 20

        # Bande semi-transparente en bas
        overlay = frame.copy()
        cv2.rectangle(
            overlay,
            (10, overlay_y),
            (w - 10, overlay_y + overlay_h),
            BG_COLOR,
            -1,
        )
        alpha = 0.55
        frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

        # Texte
        for i, line in enumerate(display_lines):
            y = overlay_y + padding + (i + 1) * line_height - 5
            cv2.putText(
                frame, line, (20, y),
                FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS, cv2.LINE_AA,
            )

    return frame


# ── WebSocket (audio → transcription) ───────────────────────────

async def websocket_handler():
    """Connexion websocket vers vLLM Realtime API."""
    global transcription_text, is_running

    async with websockets.connect(ws_url) as ws:
        # Attendre session.created
        await ws.recv()

        # Configurer le modèle
        await ws.send(json.dumps({
            "type": "session.update",
            "model": model_name,
        }))

        # Signaler prêt
        await ws.send(json.dumps({"type": "input_audio_buffer.commit"}))

        async def send_audio():
            while is_running:
                try:
                    chunk = await asyncio.get_event_loop().run_in_executor(
                        None, lambda: audio_queue.get(timeout=0.1)
                    )
                    await ws.send(json.dumps({
                        "type": "input_audio_buffer.append",
                        "audio": chunk,
                    }))
                except queue.Empty:
                    continue

        async def receive_transcription():
            global transcription_text
            async for message in ws:
                data = json.loads(message)
                if data.get("type") == "transcription.delta":
                    transcription_text += data["delta"]

        await asyncio.gather(send_audio(), receive_transcription())


def start_websocket():
    """Démarrer la boucle websocket dans un thread."""
    global is_running
    is_running = True
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(websocket_handler())
    except Exception as e:
        print(f"❌ WebSocket error: {e}")


# ── Callbacks Gradio ─────────────────────────────────────────────

def start_recording():
    """Démarrer la transcription + la caméra."""
    global transcription_text, cap
    transcription_text = ""

    # Ouvrir la caméra
    if cap is None or not cap.isOpened():
        try:
            cap = open_camera()
        except RuntimeError as e:
            return (
                gr.update(interactive=True),
                gr.update(interactive=False),
                None,
                f"⚠️ {e}",
            )

    # Lancer le websocket
    thread = threading.Thread(target=start_websocket, daemon=True)
    thread.start()

    return (
        gr.update(interactive=False),
        gr.update(interactive=True),
        None,
        "",
    )


def stop_recording():
    """Arrêter la transcription."""
    global is_running
    is_running = False
    return (
        gr.update(interactive=True),
        gr.update(interactive=False),
        None,
        transcription_text,
    )


def process_audio(audio):
    """Recevoir l'audio micro, ré-échantillonner et envoyer au WS."""
    if audio is None or not is_running:
        return grab_frame_with_overlay(), transcription_text

    sample_rate, audio_data = audio

    # Mono
    if len(audio_data.shape) > 1:
        audio_data = audio_data.mean(axis=1)

    # Float32
    if audio_data.dtype == np.int16:
        audio_float = audio_data.astype(np.float32) / 32767.0
    else:
        audio_float = audio_data.astype(np.float32)

    # Resampler à 16 kHz si nécessaire
    if sample_rate != SAMPLE_RATE:
        num_samples = int(len(audio_float) * SAMPLE_RATE / sample_rate)
        audio_float = np.interp(
            np.linspace(0, len(audio_float) - 1, num_samples),
            np.arange(len(audio_float)),
            audio_float,
        )

    # PCM16 → Base64
    pcm16 = (audio_float * 32767).astype(np.int16)
    b64_chunk = base64.b64encode(pcm16.tobytes()).decode("utf-8")
    audio_queue.put(b64_chunk)

    return grab_frame_with_overlay(), transcription_text


def update_video():
    """Rafraîchir le flux vidéo (appelé en polling)."""
    return grab_frame_with_overlay()


# ── Interface Gradio ─────────────────────────────────────────────

def build_demo():
    with gr.Blocks(
        title="Voxtral Realtime — Caméra + Transcription",
        theme=gr.themes.Soft(primary_hue="blue"),
    ) as demo:
        gr.Markdown(
            "# 🎙️ Voxtral Realtime — Prototype\n"
            "Flux caméra avec transcription audio temps-réel.\n\n"
            "1. Lancer le serveur : `bash serve.sh`\n"
            "2. Cliquer **▶ Start** et parler dans le micro."
        )

        with gr.Row():
            start_btn = gr.Button("▶ Start", variant="primary", scale=1)
            stop_btn = gr.Button("⏹ Stop", variant="stop", interactive=False, scale=1)

        with gr.Row():
            video_output = gr.Image(
                label="📹 Caméra + Sous-titres",
                type="numpy",
                height=480,
            )

        audio_input = gr.Audio(
            sources=["microphone"],
            streaming=True,
            type="numpy",
            label="🎤 Microphone",
        )

        transcript_box = gr.Textbox(
            label="📝 Transcription complète",
            lines=5,
            interactive=False,
        )

        # Événements
        start_btn.click(
            start_recording,
            outputs=[start_btn, stop_btn, video_output, transcript_box],
        )
        stop_btn.click(
            stop_recording,
            outputs=[start_btn, stop_btn, video_output, transcript_box],
        )
        audio_input.stream(
            process_audio,
            inputs=[audio_input],
            outputs=[video_output, transcript_box],
        )

        # Polling vidéo à ~10 fps via un timer
        timer = gr.Timer(value=0.1)
        timer.tick(update_video, outputs=[video_output])

    return demo


# ── Main ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Voxtral Realtime — Caméra + Transcription"
    )
    parser.add_argument(
        "--model", type=str,
        default="mistralai/Voxtral-Mini-4B-Realtime-2602",
        help="Modèle servi par vLLM",
    )
    parser.add_argument("--host", type=str, default="localhost", help="Hôte vLLM")
    parser.add_argument("--port", type=int, default=8000, help="Port vLLM")
    parser.add_argument("--camera", type=int, default=0, help="Index caméra (0, 1…)")
    parser.add_argument("--share", action="store_true", help="Lien Gradio public")

    args = parser.parse_args()

    ws_url = f"ws://{args.host}:{args.port}/v1/realtime"
    model_name = args.model

    # Pré-ouvrir la caméra
    try:
        cap = open_camera(args.camera)
        print(f"✅ Caméra ouverte (device={args.camera})")
    except RuntimeError as e:
        print(f"⚠️  {e} — la caméra sera tentée au démarrage.")

    print(f"🔗 Serveur vLLM attendu sur: {ws_url}")

    demo = build_demo()
    demo.launch(share=args.share)
