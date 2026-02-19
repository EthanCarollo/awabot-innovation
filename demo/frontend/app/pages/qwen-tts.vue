<template>
  <div class="container">
    <header class="header">
      <div class="header-left">
        <div class="title-row">
          <h1 class="title">Qwen3 TTS</h1>
          <StatusBadge :status="status" />
        </div>
        <p class="subtitle">Synthese vocale naturelle et clonage de voix via Qwen3 0.6B.</p>
      </div>
    </header>

    <div class="layout-grid">
      <!-- Input Column -->
      <div class="column-input">
        <!-- Configuration Card -->
        <div class="card config-card">
          <div class="card-label">1. Configuration de la voix</div>
          
          <div class="input-grid-2col">
            <div class="input-group">
              <label class="field-label">Langue du texte</label>
              <select v-model="language" class="select-input">
                <option v-for="lang in languages" :key="lang" :value="lang">{{ lang }}</option>
              </select>
            </div>

            <div class="input-group">
              <label class="field-label">Reference Vocale</label>
              <div class="voice-ref-actions">
                <div class="file-upload-wrapper" :class="{ 'has-file': !!promptAudioFile && !isRecordingRef }">
                  <input 
                    type="file" 
                    id="clone-audio" 
                    accept="audio/*" 
                    class="file-input" 
                    @change="handleFileChange"
                    :disabled="isRecordingRef"
                  />
                  <label for="clone-audio" class="file-label">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v4a2 2 0 0 1 2-2h14"/>
                      <polyline points="17 8 12 3 7 8"/>
                      <line x1="12" y1="3" x2="12" y2="15"/>
                    </svg>
                    <span>{{ promptAudioFile && !isRecordingRef ? 'Fichier prêt' : 'Envoyer...' }}</span>
                  </label>
                  <button v-if="promptAudioFile && !isRecordingRef" class="btn-clear-file" @click.stop="clearFile">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="18" y1="6" x2="6" y2="18"></line>
                      <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                  </button>
                </div>

                <div class="record-ref-wrapper">
                  <button 
                    class="btn-record-ref" 
                    :class="{ 'is-recording': isRecordingRef }"
                    @click="toggleRefRecording"
                  >
                    <div v-if="!isRecordingRef" class="mic-icon">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                        <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                        <line x1="12" y1="19" x2="12" y2="23"/>
                        <line x1="8" y1="23" x2="16" y2="23"/>
                      </svg>
                    </div>
                    <div v-else class="stop-box"></div>
                    <span>{{ isRecordingRef ? 'Arrêter' : 'Enregistrer' }}</span>
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div v-if="promptAudioFile" class="input-group mt-16 animate-in">
            <label class="field-label">Transcription de la référence</label>
            <textarea
              v-model="promptText"
              class="textarea textarea-sm"
              rows="2"
              placeholder="Tapez exactement ce que vous avez dit..."
            />
            <p class="hint">Indispensable pour que le clonage soit parfait.</p>
          </div>
          <p v-else class="hint">Utilisez un fichier ou enregistrez-vous pour cloner votre voix.</p>
        </div>

        <div class="spacer-v"></div>

        <!-- Synthesizer Card -->
        <div class="card input-card">
          <div class="card-label">2. Synthetiseur</div>
          
          <div class="input-group">
            <label for="tts-input" class="field-label">Texte a generer</label>
            <textarea
              id="tts-input"
              v-model="inputText"
              class="textarea"
              rows="4"
              placeholder="Ex: Bonjour, je suis la brique TTS d'Awabot..."
            />
          </div>

          <div class="input-footer">
            <div class="char-info">
              <span class="count">{{ inputText.length }}</span>
              <span class="limit">/ 500</span>
            </div>
            <button 
              class="btn btn-primary" 
              @click="generate" 
              :disabled="!inputText.trim() || isGenerating"
            >
              <div v-if="isGenerating" class="loader"></div>
              <span>{{ isGenerating ? 'Generation…' : 'Synthetiser' }}</span>
            </button>
          </div>
        </div>

        <div class="spacer-v"></div>

        <!-- Info Card -->
        <div class="card info-card">
          <div class="card-label">Fiche Technique</div>
          <div class="info-grid">
            <div class="info-field">
              <span class="info-key">Modele</span>
              <code class="info-val">Qwen3-TTS-0.6B</code>
            </div>
            <div class="info-field">
              <span class="info-key">Frequence</span>
              <code class="info-val">12Hz (Flow)</code>
            </div>
          </div>
          <p class="info-desc">
            Ce modele compact permet de cloner n'importe quelle voix a partir d'un simple echantillon audio, tout en conservant une expressivite naturelle.
          </p>
          <a href="https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base" target="_blank" class="hf-btn">
            <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="" />
            Hugging Face Repository
          </a>
        </div>
      </div>

      <!-- Result Column -->
      <div class="column-result">
        <div class="card result-card">
          <div class="card-label">Resultat</div>
          
          <div class="result-viewport">
            <div v-if="errorMsg" class="error-state">
              <div class="error-icon">!</div>
              <p>{{ errorMsg }}</p>
            </div>
            
            <div v-else-if="audioSrc" class="audio-state">
              <div class="audio-illustration">
                <div class="waveform-anim">
                  <div class="w-bar" v-for="i in 8" :key="i"></div>
                </div>
              </div>
              <audio :src="audioSrc" controls class="player" />
              <p class="audio-meta">Synthese terminee avec succes</p>
            </div>

            <div v-else-if="isGenerating" class="loading-state">
              <div class="loading-anim"></div>
              <p>L'IA prepare votre audio...</p>
            </div>

            <div v-else class="empty-state">
              <div class="empty-icon">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">
                  <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                  <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                  <line x1="12" y1="19" x2="12" y2="23"/>
                  <line x1="8" y1="23" x2="16" y2="23"/>
                </svg>
              </div>
              <p>Pret pour la generation</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onUnmounted } from 'vue'

const wsUrl = `ws://localhost:8084/ws/qwen-tts`

const status = ref<'idle' | 'connecting' | 'connected' | 'generating' | 'error'>('idle')
const isGenerating = ref(false)
const inputText = ref('')
const promptText = ref('')
const language = ref('French')
const promptAudioFile = ref<File | null>(null)
const audioSrc = ref('')
const errorMsg = ref('')

const isRecordingRef = ref(false)
let mediaRecorder: MediaRecorder | null = null
let audioChunks: Blob[] = []

const languages = ['French', 'English', 'Chinese', 'Japanese', 'Spanish', 'German', 'Italian']

let ws: WebSocket | null = null

function handleFileChange(event: Event) {
  const target = event.target as HTMLInputElement
  if (target.files && target.files[0]) {
    promptAudioFile.value = target.files[0]
  }
}

async function toggleRefRecording() {
  if (isRecordingRef.value) {
    mediaRecorder?.stop()
    isRecordingRef.value = false
    return
  }

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    mediaRecorder = new MediaRecorder(stream)
    audioChunks = []

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data)
    }

    mediaRecorder.onstop = async () => {
      const audioBlob = new Blob(audioChunks, { type: 'audio/wav' })
      promptAudioFile.value = new File([audioBlob], 'recording.wav', { type: 'audio/wav' })
      stream.getTracks().forEach(t => t.stop())
    }

    mediaRecorder.start()
    isRecordingRef.value = true
    errorMsg.value = ""
  } catch (err) {
    console.error("Error accessing microphone:", err)
    errorMsg.value = "Impossible d'accéder au microphone."
  }
}

function clearFile() {
  if (isRecordingRef.value) toggleRefRecording()
  promptAudioFile.value = null
  promptText.value = ''
  const input = document.getElementById('clone-audio') as HTMLInputElement
  if (input) input.value = ''
}

function connectWs(): Promise<void> {
  return new Promise((resolve, reject) => {
    status.value = 'connecting'
    ws = new WebSocket(wsUrl)
    ws.onopen = () => { status.value = 'connected' }
    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data)
      if (msg.type === 'status') {
        if (msg.message === 'connected') { status.value = 'connected'; resolve() }
        else if (msg.message === 'generating') { status.value = 'generating' }
      } else if (msg.type === 'audio') {
        const bin = atob(msg.data)
        const bytes = new Uint8Array(bin.length)
        for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i)
        audioSrc.value = URL.createObjectURL(new Blob([bytes], { type: 'audio/wav' }))
        isGenerating.value = false
        status.value = 'connected'
      } else if (msg.type === 'error') {
        errorMsg.value = msg.message
        isGenerating.value = false
        status.value = 'error'
      }
    }
    ws.onerror = () => { status.value = 'error'; reject() }
    ws.onclose = () => { if (isGenerating.value) status.value = 'error' }
  })
}

async function fileToBase64(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onload = () => {
      const b64 = (reader.result as string | null)?.split(',')[1]
      if (b64) resolve(b64)
      else reject(new Error("Failed to convert file to base64"))
    }
    reader.onerror = (error) => reject(error)
  })
}

async function generate() {
  if (!inputText.value.trim()) return
  errorMsg.value = ''
  audioSrc.value = ''
  isGenerating.value = true
  
  let promptAudioB64 = null
  if (promptAudioFile.value) {
    try {
      promptAudioB64 = await fileToBase64(promptAudioFile.value)
    } catch (e) {
      errorMsg.value = "Erreur lors de la lecture du fichier audio."
      isGenerating.value = false
      return
    }
  }

  try {
    if (!ws || ws.readyState !== WebSocket.OPEN) await connectWs()
    ws!.send(JSON.stringify({ 
      type: 'tts', 
      text: inputText.value.trim(),
      language: language.value,
      prompt_audio: promptAudioB64,
      prompt_text: promptText.value.trim()
    }))
  } catch {
    errorMsg.value = 'Impossible de se connecter au serveur de synthese.'
    isGenerating.value = false
    status.value = 'error'
  }
}

onUnmounted(() => { ws?.close(); ws = null })
</script>

<style scoped>
.container { max-width: 1100px; margin: 0 auto; padding: 60px 40px; }

/* Header */
.header { margin-bottom: 40px; }
.title-row { display: flex; align-items: center; gap: 16px; margin-bottom: 4px; }
.title { font-size: 32px; font-weight: 900; letter-spacing: -1px; color: var(--carbon); }
.subtitle { font-size: 15px; color: var(--text-muted); font-weight: 500; }

/* Layout */
.layout-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 32px;
}

@media (max-width: 900px) {
  .layout-grid { grid-template-columns: 1fr; }
}

.card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 32px; display: flex; flex-direction: column; }
.card-label { font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); margin-bottom: 24px; }

.spacer-v { height: 24px; }

/* Input Card */
.input-grid-2col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
.input-group { margin-bottom: 0px; }
.mt-16 { margin-top: 16px; }

.field-label { display: block; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; color: var(--carbon); margin-bottom: 12px; }

.select-input {
  width: 100%;
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid var(--border);
  background: var(--bg);
  font-family: inherit;
  font-size: 14px;
  font-weight: 600;
  outline: none;
  cursor: pointer;
  transition: all 0.2s;
}
.select-input:focus { border-color: var(--yellow); background: white; }

.file-upload-wrapper {
  position: relative;
  border: 2px dashed var(--border);
  border-radius: 14px;
  padding: 10px 16px;
  background: var(--bg);
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 12px;
}
.file-upload-wrapper:hover { border-color: var(--yellow); background: #FAC13005; }
.file-upload-wrapper.has-file { border-style: solid; border-color: var(--yellow); background: white; }

.file-input { position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; cursor: pointer; }
.file-label { display: flex; align-items: center; gap: 10px; color: var(--text-muted); font-size: 13px; font-weight: 600; flex: 1; pointer-events: none; overflow: hidden; }
.file-label span { white-space: nowrap; text-overflow: ellipsis; overflow: hidden; }
.file-upload-wrapper.has-file .file-label { color: var(--carbon); }

.voice-ref-actions { display: flex; gap: 12px; align-items: stretch; }
.file-upload-wrapper { flex: 1; margin-bottom: 0px !important; }

.btn-record-ref {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  height: 100%;
  padding: 0 20px;
  border-radius: 14px;
  border: 1px solid var(--border);
  background: white;
  color: var(--carbon);
  font-family: inherit;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-record-ref:hover { border-color: #f43f5e; color: #f43f5e; background: #fff1f2; }
.btn-record-ref.is-recording { background: #f43f5e; border-color: #f43f5e; color: white; animation: pulse-red 2s infinite; }

.stop-box { width: 10px; height: 10px; background: currentColor; border-radius: 2px; }

@keyframes pulse-red {
  0% { box-shadow: 0 0 0 0 rgba(244, 63, 94, 0.4); }
  70% { box-shadow: 0 0 0 10px rgba(244, 63, 94, 0); }
  100% { box-shadow: 0 0 0 0 rgba(244, 63, 94, 0); }
}

.btn-clear-file {
  position: relative;
  z-index: 1;
  background: var(--bg);
  border: 1px solid var(--border);
  color: var(--text-muted);
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-clear-file:hover { background: #fee2e2; color: #ef4444; border-color: #fca5a5; }

.hint { font-size: 11px; color: var(--text-muted); margin-top: 8px; font-weight: 500; }

.textarea {
  width: 100%; 
  font-family: inherit; 
  font-size: 15px; 
  line-height: 1.6;
  background: var(--bg); 
  color: var(--text); 
  border: 1px solid var(--border); 
  border-radius: 14px;
  padding: 16px; 
  resize: vertical; 
  outline: none; 
  transition: all 0.2s;
}
.textarea:focus { border-color: var(--yellow); background: white; }
.textarea-sm { font-size: 13px; padding: 12px; }

.input-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 24px; }
.char-info { font-size: 12px; color: var(--text-muted); font-weight: 600; }
.char-info .count { color: var(--carbon); }

.btn { font-family: inherit; font-size: 14px; font-weight: 700; border: none; border-radius: 12px; cursor: pointer; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); display: inline-flex; align-items: center; justify-content: center; gap: 10px; }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }

.btn-primary { background: var(--yellow); color: var(--carbon); padding: 16px 32px; flex: 1; margin-left: 20px; }
.btn-primary:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 4px 0px rgba(0,0,0,0.05); }

/* Result Hub */
.result-card { min-height: 520px; }
.result-viewport { flex: 1; display: flex; align-items: center; justify-content: center; background: var(--bg); border-radius: 14px; padding: 32px; text-align: center; }

.empty-state, .loading-state, .error-state, .audio-state { display: flex; flex-direction: column; align-items: center; gap: 16px; width: 100%; }
.empty-icon { opacity: 0.2; margin-bottom: 8px; }
.empty-state p { font-size: 14px; font-weight: 600; color: var(--text-muted); }

.loading-anim { width: 40px; height: 40px; border: 4px solid var(--border); border-top-color: var(--yellow); border-radius: 50%; animation: spin 0.8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }

.audio-illustration { margin-bottom: 12px; }
.waveform-anim { display: flex; gap: 4px; height: 32px; align-items: center; }
.w-bar { width: 4px; height: 16px; background: var(--yellow); border-radius: 2px; animation: wave 1.2s ease-in-out infinite; }
.w-bar:nth-child(even) { animation-delay: 0.2s; }
.w-bar:nth-child(3n) { animation-delay: 0.4s; }
@keyframes wave { 0%, 100% { height: 12px; } 50% { height: 28px; } }

.player { width: 100%; border-radius: 12px; background: white; }
.audio-meta { font-size: 12px; font-weight: 600; color: #10B981; margin-top: 8px; }

/* Info Section */
.info-desc { font-size: 14px; line-height: 1.6; color: var(--text-muted); margin: 24px 0; }
.info-grid { display: flex; gap: 24px; flex-wrap: wrap; }
.info-field { display: flex; flex-direction: column; gap: 6px; }
.info-key { font-size: 9px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-muted); }
.info-val { font-family: ui-monospace, SFMono-Regular, monospace; font-size: 11px; font-weight: 600; color: #D97706; background: #FAC13010; padding: 4px 8px; border-radius: 6px; }

.hf-btn { display: inline-flex; align-items: center; gap: 10px; font-size: 13px; font-weight: 700; color: var(--carbon); text-decoration: none; padding: 12px 20px; background: var(--bg); border-radius: 10px; transition: all 0.2s; border: 1px solid var(--border); margin-top: auto; }
.hf-btn:hover { background: var(--border); }
.hf-btn img { width: 18px; }

.loader { width: 16px; height: 16px; border: 2px solid white; border-top-color: transparent; border-radius: 50%; animation: spin 0.6s linear infinite; }

.animate-in { animation: slideDown 0.3s ease-out; }
@keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
</style>
