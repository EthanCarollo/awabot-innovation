<template>
  <div class="container">
    <header class="header">
      <div class="header-left">
        <div class="title-row">
          <h1 class="title">Voice Cloning Lab</h1>
          <StatusBadge :status="status" />
        </div>
        <p class="subtitle">Enregistrez votre empreinte vocale pour générer un clone haute-fidélité.</p>
      </div>
      <div class="header-actions">
        <button class="btn btn-secondary" @click="clearTranscript" :disabled="!transcript">
          Réinitialiser
        </button>
      </div>
    </header>

    <div class="layout-grid">
      <!-- Left Panel: Vision & Interaction -->
      <div class="panel-left">
        <div class="card video-card hero-card">
          <div class="card-label">Capture de Référence</div>
          <div class="video-viewport">
            <video v-show="cameraActive" ref="videoEl" autoplay playsinline muted class="video-feed"></video>
            <div v-if="!cameraActive" class="video-placeholder">
              <div class="placeholder-art">
                <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="0.75">
                  <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                  <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                  <line x1="12" y1="19" x2="12" y2="23"/>
                  <line x1="8" y1="23" x2="16" y2="23"/>
                </svg>
              </div>
              <p>Prêt pour l'enregistrement</p>
              <span>Veuillez lire le script à voix haute pour le clonage</span>
            </div>
          </div>
        </div>

        <div class="card interaction-card">
          <div class="card-label">Enregistrement Empreinte</div>
          <div class="interaction-body">
            <div class="action-btn-wrapper">
              <button v-if="!isRecording" class="btn btn-primary btn-record" @click="toggleRecording" :disabled="status === 'connecting'">
                <div class="record-indicator">
                   <div class="pulse-ring"></div>
                   <div class="dot"></div>
                </div>
                Démarrer l'enregistrement
              </button>
              <button v-else class="btn btn-stop" @click="toggleRecording">
                <div class="stop-icon"></div>
                Finaliser l'empreinte
              </button>
            </div>
            
            <div class="visualizer-slot">
              <AudioVisualizer v-if="isRecording" :levels="audioLevel" gradient="linear-gradient(to right, #6366f1, #a855f7)" />
              <div v-else class="visualizer-idle">
                <div class="v-wave" v-for="i in 20" :key="i" :style="{ height: (3 + Math.random() * 8) + 'px' }"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Panel: Data & Intelligence -->
      <div class="panel-right">
        <div class="card transcript-card glass-effect">
          <div class="card-label">Script & Vérification</div>
          <div class="transcript-viewport" :class="{ 'is-active': isRecording }" ref="transcriptScroll">
            <div v-if="!transcript && !isRecording" class="transcript-empty">
              <p>Écoute en cours...</p>
              <span>Le texte sera validé pour assurer la qualité du clone</span>
            </div>
            <div v-else class="transcript-text">
              {{ transcript }}<span v-if="isRecording" class="typing-cursor"></span>
            </div>
          </div>
        </div>

        <div class="card tech-card">
          <div class="card-label">Intelligence du Clone</div>
          <div class="tech-content">
            <div class="tech-metrics">
              <div class="metric">
                <span class="m-label">Type</span>
                <span class="m-val">Zero-Shot</span>
              </div>
              <div class="metric">
                <span class="m-label">Qualité</span>
                <span class="m-val">44.1 kHz</span>
              </div>
              <div class="metric">
                <span class="m-label">Status</span>
                <span class="m-val">Prêt</span>
              </div>
            </div>
            <p class="tech-desc">
              Extraction des caractéristiques prosodiques et spectrales pour une synthèse vocale <strong>ultra-réaliste</strong>.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onUnmounted, watch, nextTick } from 'vue'

const videoEl = ref<HTMLVideoElement | null>(null)
const transcriptScroll = ref<HTMLElement | null>(null)
const cameraActive = ref(false)
let stream: MediaStream | null = null

const { status, isRecording, transcript, audioLevel, start, stop, clearTranscript } =
  useAudioCapture(`ws://localhost:8083/ws/qwen-asr`)

// Auto-scroll transcript to bottom
watch(transcript, () => {
  nextTick(() => {
    if (transcriptScroll.value) {
      transcriptScroll.value.scrollTop = transcriptScroll.value.scrollHeight
    }
  })
})

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

.layout-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  align-items: start;
}

@media (max-width: 1100px) {
  .layout-grid { grid-template-columns: 1fr; }
}

/* Panel Specifics */
.panel-left, .panel-right { display: flex; flex-direction: column; gap: 24px; }

/* Cards & Components */
.card { 
  background: var(--bg-card); 
  border: 1px solid var(--border); 
  border-radius: 24px; 
  padding: 32px; 
  position: relative; 
  transition: all 0.3s ease;
  box-shadow: 0 4px 20px -8px rgba(0,0,0,0.05);
}

.hero-card { padding: 8px; border-width: 2px; }
.hero-card .card-label { padding: 16px 24px 8px; margin-bottom: 12px; }

.card-label { 
  font-size: 11px; 
  font-weight: 800; 
  text-transform: uppercase; 
  letter-spacing: 1.5px; 
  color: var(--text-muted); 
  margin-bottom: 24px; 
}

/* Video Viewport */
.video-viewport {
  aspect-ratio: 16/10;
  background: var(--bg);
  border-radius: 18px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
}

.video-feed { width: 100%; height: 100%; object-fit: cover; }
.video-placeholder { text-align: center; color: var(--text-muted); padding: 40px; }
.placeholder-art { margin-bottom: 24px; opacity: 0.2; display: flex; justify-content: center; color: var(--indigo); }
.video-placeholder p { font-size: 16px; font-weight: 800; color: var(--carbon); margin-bottom: 8px; letter-spacing: -0.5px; }
.video-placeholder span { font-size: 12px; font-weight: 500; opacity: 0.7; }

/* Interaction Card */
.interaction-body { display: flex; flex-direction: column; gap: 24px; }

.btn { 
  font-family: inherit; 
  font-size: 15px; 
  font-weight: 700; 
  border: none; 
  border-radius: 16px; 
  cursor: pointer; 
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); 
  display: inline-flex; 
  align-items: center; 
  justify-content: center; 
  gap: 14px; 
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none !important; box-shadow: none !important; }

.btn-primary { background: var(--indigo); color: white; padding: 20px 32px; width: 100%; }
.btn-primary:hover:not(:disabled) { background: #4f46e5; transform: translateY(-2px); box-shadow: 0 15px 25px -5px rgba(99, 102, 241, 0.3); }

.btn-stop { background: #f43f5e; color: white; padding: 20px 32px; width: 100%; }
.btn-stop:hover { background: #e11d48; transform: translateY(-2px); box-shadow: 0 15px 25px -5px rgba(244, 63, 94, 0.3); }

.btn-secondary { background: white; border: 1px solid var(--border); color: var(--carbon); padding: 10px 24px; border-radius: 12px; }
.btn-secondary:hover:not(:disabled) { border-color: var(--indigo); color: var(--indigo); }

/* Recording Indicators */
.record-indicator { position: relative; width: 12px; height: 12px; }
.record-indicator .dot { width: 12px; height: 12px; background: white; border-radius: 50%; position: relative; z-index: 2; }
.record-indicator .pulse-ring {
  position: absolute;
  top: 0; left: 0; width: 12px; height: 12px;
  background: white; border-radius: 50%;
  animation: ripple 1.5s infinite;
}
@keyframes ripple { 0% { transform: scale(1); opacity: 0.5; } 100% { transform: scale(3.5); opacity: 0; } }

.stop-icon { width: 12px; height: 12px; background: white; border-radius: 3px; }

.visualizer-slot { 
  height: 60px; 
  display: flex; 
  align-items: center; 
  justify-content: center;
  background: #f8fafc;
  border-radius: 14px;
}
.visualizer-idle { display: flex; gap: 4px; align-items: center; }
.v-wave { width: 3px; background: var(--border); border-radius: 2px; opacity: 0.5; }

/* Transcript Card */
.transcript-card { min-height: 520px; display: flex; flex-direction: column; border-color: var(--indigo); }
.glass-effect { backdrop-filter: blur(8px); background: rgba(255, 255, 255, 0.8); }

.transcript-viewport { 
  flex: 1; 
  background: #f8fafc; 
  border-radius: 18px; 
  padding: 40px; 
  font-size: 20px; 
  line-height: 1.8; 
  color: var(--carbon); 
  overflow-y: auto;
  transition: all 0.4s;
  border: 1px solid rgba(0,0,0,0.02);
}
.transcript-viewport.is-active { background: white; border-color: rgba(99, 102, 241, 0.1); box-shadow: inset 0 2px 10px rgba(0,0,0,0.02); }

.transcript-empty { 
  color: var(--text-muted); 
  height: 100%; 
  display: flex; 
  flex-direction: column;
  align-items: center; 
  justify-content: center; 
  text-align: center; 
}
.transcript-empty p { font-weight: 700; font-size: 18px; color: var(--carbon); margin-bottom: 8px; }
.transcript-empty span { font-size: 13px; opacity: 0.6; }

.typing-cursor { display: inline-block; width: 3px; height: 1.2em; background: var(--indigo); margin-left: 6px; vertical-align: middle; animation: blink 0.8s infinite; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

/* Tech Card */
.tech-metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 24px; }
.metric { display: flex; flex-direction: column; gap: 4px; }
.m-label { font-size: 10px; font-weight: 800; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.5px; }
.m-val { font-size: 14px; font-weight: 700; color: var(--indigo); }

.tech-desc { font-size: 14px; line-height: 1.6; color: var(--text-muted); margin-bottom: 24px; }
.hf-link { 
  display: inline-flex; 
  align-items: center; 
  gap: 12px; 
  font-size: 13px; 
  font-weight: 700; 
  color: var(--carbon); 
  text-decoration: none; 
  padding: 14px 24px; 
  background: white; 
  border-radius: 12px; 
  transition: all 0.2s; 
  border: 1px solid var(--border); 
}
.hf-link:hover { border-color: var(--indigo); transform: translateY(-1px); }
.hf-link img { width: 20px; }
</style>
