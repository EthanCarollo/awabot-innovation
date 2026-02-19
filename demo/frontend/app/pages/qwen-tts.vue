<template>
  <div class="container">
    <header class="header">
      <div>
        <h1 class="title">Qwen3 TTS</h1>
        <p class="subtitle">Synthese vocale — Qwen3-TTS 0.6B</p>
      </div>
      <StatusBadge :status="status" />
    </header>

    <div class="card input-card">
      <label class="input-label" for="tts-input">Texte a synthetiser</label>
      <textarea
        id="tts-input"
        v-model="inputText"
        class="textarea"
        rows="4"
        placeholder="Entrez le texte que vous souhaitez convertir en parole…"
      />
      <div class="input-footer">
        <span class="char-count">{{ inputText.length }} caracteres</span>
        <button class="btn btn-generate" @click="generate" :disabled="!inputText.trim() || isGenerating">
          {{ isGenerating ? 'Generation…' : 'Generer la voix' }}
        </button>
      </div>
    </div>

    <div class="card" v-if="audioSrc || errorMsg">
      <h2 class="section-title">Resultat</h2>
      <div v-if="errorMsg" class="error-box">{{ errorMsg }}</div>
      <div v-if="audioSrc" class="audio-player">
        <audio :src="audioSrc" controls class="player" />
        <p class="audio-info">Format: WAV — Qwen3-TTS (0.6B)</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onUnmounted } from 'vue'

const config = useRuntimeConfig()
const wsUrl = `${config.public.wsBackendBase}/ws/qwen-tts`

const status = ref<'idle' | 'connecting' | 'connected' | 'generating' | 'error'>('idle')
const isGenerating = ref(false)
const inputText = ref('')
const audioSrc = ref('')
const errorMsg = ref('')

let ws: WebSocket | null = null

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

async function generate() {
  errorMsg.value = ''
  audioSrc.value = ''
  isGenerating.value = true
  try {
    if (!ws || ws.readyState !== WebSocket.OPEN) await connectWs()
    ws!.send(JSON.stringify({ type: 'tts', text: inputText.value.trim() }))
  } catch {
    errorMsg.value = 'Impossible de se connecter au backend.'
    isGenerating.value = false
    status.value = 'error'
  }
}

onUnmounted(() => { ws?.close(); ws = null })
</script>

<style scoped>
.container { max-width: 720px; margin: 0 auto; padding: 40px 20px; }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
.title { font-size: 22px; font-weight: 800; letter-spacing: -0.5px; }
.subtitle { font-size: 13px; color: var(--text-muted); }
.card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 24px; margin-bottom: 16px; }
.section-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); margin-bottom: 16px; }
.input-label { display: block; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); margin-bottom: 12px; }
.textarea {
  width: 100%; font-family: inherit; font-size: 15px; line-height: 1.6;
  background: var(--bg); color: var(--text); border: 1px solid var(--border); border-radius: 12px;
  padding: 16px; resize: vertical; outline: none; transition: border-color .2s;
}
.textarea:focus { border-color: var(--orange); }
.textarea::placeholder { color: var(--text-muted); }
.input-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 16px; }
.char-count { font-size: 12px; color: var(--text-muted); }
.btn { font-family: inherit; font-size: 15px; font-weight: 700; padding: 12px 28px; border: none; border-radius: 12px; cursor: pointer; transition: all .2s; }
.btn:disabled { opacity: .5; cursor: not-allowed; }
.btn-generate { background: var(--yellow); color: var(--carbon); }
.btn-generate:hover:not(:disabled) { opacity: 0.85; }
.error-box { background: rgba(239,68,68,.06); border: 1px solid rgba(239,68,68,.2); border-radius: 12px; padding: 16px; color: #dc2626; font-size: 14px; margin-bottom: 16px; }
.audio-player { text-align: center; }
.player { width: 100%; border-radius: 12px; margin-bottom: 8px; }
.audio-info { font-size: 12px; color: var(--text-muted); }
</style>
