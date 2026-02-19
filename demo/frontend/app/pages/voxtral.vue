<template>
  <div class="container">
    <header class="header">
      <div class="header-left">
        <div class="title-row">
          <h1 class="title">Voxtral ASR</h1>
          <StatusBadge :status="status" />
        </div>
        <p class="subtitle">Transcription temps reel via Mistral Voxtral Mini 4B.</p>
      </div>
      <div class="header-actions">
        <button class="btn btn-secondary" @click="clearTranscript" :disabled="!transcript">
          Effacer
        </button>
      </div>
    </header>

    <div class="layout-grid">
      <!-- Media Column -->
      <div class="column-media">
        <div class="card video-card">
          <div class="card-label">Flux Video</div>
          <div class="video-viewport">
            <video v-show="cameraActive" ref="videoEl" autoplay playsinline muted class="video-feed"></video>
            <div v-if="!cameraActive" class="video-placeholder">
              <div class="placeholder-art">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">
                  <path d="M23 7l-7 5 7 5V7z"/>
                  <rect x="1" y="5" width="15" height="14" rx="3" ry="3"/>
                  <circle cx="8.5" cy="12" r="1.5"/>
                </svg>
              </div>
              <p>Camera inactive</p>
              <span>Lancez la transcription pour activer la camera</span>
            </div>
          </div>
        </div>

        <div class="card controls-card">
          <div class="card-label">Controles</div>
          <div class="controls-body">
            <div class="action-btn-wrapper">
              <button v-if="!isRecording" class="btn btn-primary btn-record" @click="toggleRecording" :disabled="status === 'connecting'">
                <div class="record-dot"></div>
                Demarrer la transcription
              </button>
              <button v-else class="btn btn-stop" @click="toggleRecording">
                <div class="stop-square"></div>
                Arreter la capture
              </button>
            </div>
            
            <div class="visualizer-container">
              <AudioVisualizer v-if="isRecording" :levels="audioLevel" />
              <div v-else class="visualizer-placeholder">
                <div class="v-bar" v-for="i in 12" :key="i"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Content Column -->
      <div class="column-content">
        <div class="card transcript-card">
          <div class="card-label">Transcription</div>
          <div class="transcript-viewport" :class="{ 'is-active': isRecording }">
            <div v-if="!transcript && !isRecording" class="transcript-empty">
              Les paroles s'afficheront ici en temps reel...
            </div>
            <div v-else class="transcript-text">
              {{ transcript }}<span v-if="isRecording" class="typing-cursor"></span>
            </div>
          </div>
        </div>

        <div class="card info-card">
          <div class="card-label">Fiche Technique</div>
          <div class="info-grid">
            <div class="info-field">
              <span class="info-key">Modele</span>
              <code class="info-val">Voxtral-Mini-4B</code>
            </div>
            <div class="info-field">
              <span class="info-key">Type</span>
              <code class="info-val">Unified Speech-to-Text</code>
            </div>
          </div>
          <p class="info-desc">
            Optimise pour le streaming, ce modele traite l'audio directement sans etape de modularisation intermediaire (CTC/RNN-T).
          </p>
          <a href="https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602" target="_blank" class="hf-btn">
            <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="" />
            Hugging Face Repository
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onUnmounted } from 'vue'

const videoEl = ref<HTMLVideoElement | null>(null)
const cameraActive = ref(false)
let stream: MediaStream | null = null

const wsBase = 'ws://localhost:8082' 
const { status, isRecording, transcript, audioLevel, start, stop, clearTranscript } =
  useAudioCapture(`${wsBase}/ws/voxtral`)

async function startCamera() {
  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: true })
    if (videoEl.value) {
      videoEl.value.srcObject = stream
      cameraActive.value = true
    }
  } catch (err) {
    console.error("Error accessing camera:", err)
  }
}

function stopCamera() {
  if (stream) {
    stream.getTracks().forEach(track => track.stop())
    stream = null
    cameraActive.value = false
  }
}

async function toggleRecording() {
  if (isRecording.value) {
    stop()
    stopCamera()
  } else {
    await start()
    await startCamera()
  }
}

onUnmounted(() => {
  stopCamera()
})
</script>

<style scoped>
.container { max-width: 1200px; margin: 0 auto; padding: 60px 40px; }

/* Header */
.header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 40px; }
.title-row { display: flex; align-items: center; gap: 16px; margin-bottom: 4px; }
.title { font-size: 32px; font-weight: 900; letter-spacing: -1px; color: var(--carbon); }
.subtitle { font-size: 15px; color: var(--text-muted); font-weight: 500; }

/* Layout Grid */
.layout-grid {
  display: grid;
  grid-template-columns: 460px 1fr;
  gap: 24px;
}

@media (max-width: 1024px) {
  .layout-grid { grid-template-columns: 1fr; }
}

/* Cards & Components */
.card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 32px; position: relative; margin-bottom: 24px; }
.card-label { font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); margin-bottom: 24px; }

/* Video Viewport */
.video-viewport {
  aspect-ratio: 16/9;
  background: var(--bg);
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-feed { width: 100%; height: 100%; object-fit: cover; }
.video-placeholder { text-align: center; color: var(--text-muted); }
.placeholder-art { margin-bottom: 16px; opacity: 0.4; display: flex; justify-content: center; }
.video-placeholder p { font-size: 13px; font-weight: 800; color: var(--carbon); margin-bottom: 4px; }
.video-placeholder span { font-size: 11px; font-weight: 500; }

/* Controls */
.controls-body { display: flex; flex-direction: column; gap: 32px; }
.btn { font-family: inherit; font-size: 14px; font-weight: 700; border: none; border-radius: 12px; cursor: pointer; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); display: inline-flex; align-items: center; justify-content: center; gap: 10px; }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }

.btn-primary { background: var(--orange); color: white; padding: 16px 32px; width: 100%; }
.btn-primary:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 4px 0px rgba(0,0,0,0.05); }

.btn-stop { background: #EF4444; color: white; padding: 16px 32px; width: 100%; }
.btn-stop:hover { transform: translateY(-2px); box-shadow: 0 4px 0px rgba(0,0,0,0.05); }

.btn-secondary { background: white; border: 1px solid var(--border); color: var(--carbon); padding: 10px 20px; }
.btn-secondary:hover:not(:disabled) { background: var(--bg); }

.record-dot { width: 10px; height: 10px; background: white; border-radius: 50%; animation: pulse 1.5s infinite; }
.stop-square { width: 10px; height: 10px; background: white; border-radius: 2px; }

@keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }

.visualizer-container { height: 40px; display: flex; align-items: center; justify-content: center; }
.visualizer-placeholder { display: flex; gap: 3px; align-items: center; }
.v-bar { width: 3px; height: 6px; background: var(--border); border-radius: 1px; }

/* Transcript Viewport */
.transcript-card { min-height: 400px; display: flex; flex-direction: column; }
.transcript-viewport { 
  flex: 1; 
  background: var(--bg); 
  border-radius: 14px; 
  padding: 32px; 
  font-size: 18px; 
  line-height: 1.8; 
  color: var(--carbon); 
  overflow-y: auto;
  transition: all 0.3s;
  border: 1px solid transparent;
}
.transcript-viewport.is-active { background: white; border-color: var(--orange); }
.transcript-empty { color: var(--text-muted); font-style: italic; font-size: 16px; display: flex; height: 100%; align-items: center; justify-content: center; text-align: center; opacity: 0.6; }

.typing-cursor { display: inline-block; width: 8px; height: 20px; background: var(--orange); margin-left: 4px; vertical-align: middle; animation: blink 1s infinite; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

/* Info Card */
.info-desc { font-size: 14px; line-height: 1.6; color: var(--text-muted); margin: 24px 0; }
.info-grid { display: flex; gap: 24px; }
.info-field { display: flex; flex-direction: column; gap: 6px; }
.info-key { font-size: 9px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-muted); }
.info-val { font-family: ui-monospace, SFMono-Regular, monospace; font-size: 11px; font-weight: 600; color: var(--orange); background: #FF7E2208; padding: 4px 8px; border-radius: 6px; }

.hf-btn { display: inline-flex; align-items: center; gap: 10px; font-size: 13px; font-weight: 700; color: var(--carbon); text-decoration: none; padding: 12px 20px; background: var(--bg); border-radius: 10px; transition: all 0.2s; border: 1px solid var(--border); }
.hf-btn:hover { background: var(--border); }
.hf-btn img { width: 18px; }
</style>
