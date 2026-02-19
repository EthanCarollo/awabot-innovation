<template>
  <div class="container">
    <header class="header">
      <div>
        <h1 class="title">Qwen3 ASR</h1>
        <p class="subtitle">Transcription temps reel — Qwen3-ASR 1.7B</p>
      </div>
      <StatusBadge :status="status" />
    </header>

    <div class="main-grid">
      <!-- Camera Preview Column -->
      <div class="card video-card">
        <div class="card-header">
          <h2>Video Preview</h2>
        </div>
        <div class="video-container">
          <video v-show="cameraActive" ref="videoEl" autoplay playsinline muted class="video-feed"></video>
          <div v-if="!cameraActive" class="video-placeholder">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M23 7l-7 5 7 5V7z"/>
              <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
            </svg>
            <p>Camera inactive</p>
          </div>
        </div>
      </div>

      <!-- Controls & Visualizer Column -->
      <div class="card controls-card">
        <div class="controls">
          <button v-if="!isRecording" class="btn btn-start" @click="toggleRecording" :disabled="status === 'connecting'">
            Demarrer
          </button>
          <button v-else class="btn btn-stop" @click="toggleRecording">
            Arreter
          </button>
        </div>
        <AudioVisualizer
          v-if="isRecording"
          :levels="audioLevel"
          gradient="linear-gradient(to top, #6366f1, #818cf8)"
        />
        <p class="hint" v-else>Cliquez pour commencer la transcription en temps reel</p>
      </div>
    </div>

    <TranscriptPanel
      :text="transcript"
      :active="isRecording"
      cursor-color="#6366f1"
      @clear="clearTranscript"
    />

    <!-- Model Info Section -->
    <div class="card info-card">
      <div class="card-header">
        <h2>A propos du modele</h2>
      </div>
      <div class="info-content">
        <div class="info-item">
          <strong>Modele :</strong>
          <code>Qwen/Qwen3-ASR-1.7B</code>
        </div>
        <div class="info-item">
          <strong>Description :</strong>
          Modèle ASR et LID de bout en bout couvrant 52 langues et dialectes, offrant des performances de pointe parmi les modèles open-source.
        </div>
        <div class="info-footer">
          <a href="https://huggingface.co/Qwen/Qwen3-ASR-1.7B" target="_blank" class="hf-link">
            <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="HF" class="hf-logo" />
            Voir sur Hugging Face
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

const { status, isRecording, transcript, audioLevel, start, stop, clearTranscript } =
  useAudioCapture(`ws://localhost:8083/ws/qwen-asr`)

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
.container { max-width: 960px; margin: 0 auto; padding: 40px 20px; }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
.title { font-size: 22px; font-weight: 800; letter-spacing: -0.5px; }
.subtitle { font-size: 13px; color: var(--text-muted); }

.main-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 16px;
}

@media (max-width: 768px) {
  .main-grid { grid-template-columns: 1fr; }
}

.card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 24px; margin-bottom: 16px; }

.card-header h2 {
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-muted);
  margin-bottom: 12px;
}

.video-container {
  aspect-ratio: 16/9;
  background: var(--bg);
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-feed {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.video-placeholder {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  color: var(--text-muted);
  width: 100%;
  text-align: center;
}

.video-placeholder p { font-size: 12px; font-weight: 600; }

.controls { text-align: center; margin-bottom: 16px; }
.btn { display: inline-flex; align-items: center; gap: 10px; font-family: inherit; font-size: 15px; font-weight: 700; padding: 14px 32px; border: none; border-radius: 12px; cursor: pointer; transition: all .2s; }
.btn:disabled { opacity: .5; cursor: not-allowed; }
.btn-start { background: #6366f1; color: #fff; }
.btn-start:hover:not(:disabled) { opacity: 0.85; }
.btn-stop { background: #ef4444; color: #fff; }
.btn-stop:hover { opacity: 0.85; }
.hint { font-size: 13px; color: var(--text-muted); text-align: center; }

/* Info Section */
.info-card { margin-top: 16px; }
.info-content { font-size: 14px; line-height: 1.6; color: var(--text); }
.info-item { margin-bottom: 12px; }
.info-item code { background: var(--bg); padding: 2px 6px; border-radius: 4px; font-size: 13px; color: #6366f1; }
.info-footer { margin-top: 20px; border-top: 1px solid var(--border); pt: 16px; }
.hf-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--text);
  text-decoration: none;
  font-weight: 600;
  font-size: 13px;
  padding: 8px 16px;
  background: var(--bg);
  border-radius: 8px;
  transition: all 0.2s;
}
.hf-link:hover { background: var(--border); }
.hf-logo { width: 20px; height: 20px; }
</style>
