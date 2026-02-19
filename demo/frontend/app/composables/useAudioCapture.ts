/**
 * useAudioCapture — Composable for mic capture, resampling, and WebSocket streaming.
 */
import { ref, onUnmounted } from 'vue'

export function useAudioCapture(wsUrl: string) {
    const status = ref<'idle' | 'connecting' | 'connected' | 'ready' | 'error'>('idle')
    const isRecording = ref(false)
    const transcript = ref('')
    const audioLevel = ref<number[]>(new Array(24).fill(4))

    let ws: WebSocket | null = null
    let audioContext: AudioContext | null = null
    let mediaStream: MediaStream | null = null
    let processor: ScriptProcessorNode | null = null

    // ── Audio utils ──
    function floatTo16BitPCM(f: Float32Array): Int16Array {
        const o = new Int16Array(f.length)
        for (let i = 0; i < f.length; i++) {
            const s = Math.max(-1, Math.min(1, f[i]))
            o[i] = s < 0 ? s * 0x8000 : s * 0x7FFF
        }
        return o
    }

    function resample(buf: Float32Array, from: number, to: number): Float32Array {
        if (from === to) return buf
        const ratio = from / to
        const newLen = Math.round(buf.length / ratio)
        const out = new Float32Array(newLen)
        for (let i = 0; i < newLen; i++) {
            const pos = i * ratio
            const idx = Math.floor(pos)
            const frac = pos - idx
            out[i] = idx + 1 < buf.length
                ? buf[idx]! * (1 - frac) + buf[idx + 1]! * frac
                : buf[idx]!
        }
        return out
    }

    function toBase64(buffer: ArrayBuffer): string {
        const bytes = new Uint8Array(buffer)
        let binary = ''
        for (let i = 0; i < bytes.byteLength; i++) {
            binary += String.fromCharCode(bytes[i]!)
        }
        return btoa(binary)
    }

    // ── Start ──
    async function start() {
        transcript.value = ''
        status.value = 'connecting'

        ws = new WebSocket(wsUrl)
        ws.onopen = () => { status.value = 'connected' }
        ws.onmessage = (e) => {
            const m = JSON.parse(e.data)
            if (m.type === 'status' && m.message === 'ready') status.value = 'ready'
            else if (m.type === 'transcript') transcript.value += m.text
            else if (m.type === 'error') { console.error(m.message); status.value = 'error' }
        }
        ws.onerror = () => { status.value = 'error' }
        ws.onclose = () => { if (isRecording.value) status.value = 'error' }

        try {
            mediaStream = await navigator.mediaDevices.getUserMedia({
                audio: { sampleRate: 16000, channelCount: 1, echoCancellation: true, noiseSuppression: true },
            })
            audioContext = new AudioContext({ sampleRate: 16000 })
            const src = audioContext.createMediaStreamSource(mediaStream)
            processor = audioContext.createScriptProcessor(4096, 1, 1)

            processor.onaudioprocess = (ev) => {
                if (!isRecording.value || !ws || ws.readyState !== WebSocket.OPEN) return
                const data = ev.inputBuffer.getChannelData(0)

                // Update visualizer levels
                const bars = 24
                const chunkSize = Math.floor(data.length / bars)
                const levels: number[] = []
                for (let i = 0; i < bars; i++) {
                    let sum = 0
                    for (let j = 0; j < chunkSize; j++) sum += Math.abs(data[i * chunkSize + j] ?? 0)
                    levels.push(Math.max(4, Math.min(48, (sum / chunkSize) * 600)))
                }
                audioLevel.value = levels

                // Send audio
                const pcm = floatTo16BitPCM(resample(data, audioContext!.sampleRate, 16000))
                ws.send(JSON.stringify({ type: 'audio', data: toBase64(pcm.buffer as ArrayBuffer) }))
            }

            src.connect(processor)
            processor.connect(audioContext.destination)
            isRecording.value = true
        } catch {
            status.value = 'error'
        }
    }

    // ── Stop ──
    function stop() {
        isRecording.value = false
        audioLevel.value = new Array(24).fill(4)
        processor?.disconnect(); processor = null
        audioContext?.close(); audioContext = null
        mediaStream?.getTracks().forEach(t => t.stop()); mediaStream = null
        ws?.close(); ws = null
        status.value = 'idle'
    }

    function clearTranscript() {
        transcript.value = ''
    }

    onUnmounted(() => stop())

    return { status, isRecording, transcript, audioLevel, start, stop, clearTranscript }
}
