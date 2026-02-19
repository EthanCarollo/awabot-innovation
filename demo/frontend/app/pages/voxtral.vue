<template>
  <div class="container">
    <header class="header">
      <div>
        <h1 class="title">Voxtral ASR</h1>
        <p class="subtitle">Transcription temps reel — Mistral Voxtral Mini 4B</p>
      </div>
      <StatusBadge :status="status" />
    </header>

    <div class="card controls-card">
      <div class="controls">
        <button v-if="!isRecording" class="btn btn-start" @click="start" :disabled="status === 'connecting'">
          Demarrer
        </button>
        <button v-else class="btn btn-stop" @click="stop">
          Arreter
        </button>
      </div>
      <AudioVisualizer v-if="isRecording" :levels="audioLevel" />
      <p class="hint" v-else>Cliquez pour commencer la transcription en temps reel</p>
    </div>

    <TranscriptPanel
      :text="transcript"
      :active="isRecording"
      cursor-color="var(--orange)"
      @clear="clearTranscript"
    />
  </div>
</template>

<script setup lang="ts">
const config = useRuntimeConfig()
const { status, isRecording, transcript, audioLevel, start, stop, clearTranscript } =
  useAudioCapture(`${config.public.wsBackendBase}/ws/voxtral`)
</script>

<style scoped>
.container { max-width: 720px; margin: 0 auto; padding: 40px 20px; }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
.title { font-size: 22px; font-weight: 800; letter-spacing: -0.5px; }
.subtitle { font-size: 13px; color: var(--text-muted); }
.card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 24px; margin-bottom: 16px; }
.controls { text-align: center; margin-bottom: 16px; }
.btn { display: inline-flex; align-items: center; gap: 10px; font-family: inherit; font-size: 15px; font-weight: 700; padding: 14px 32px; border: none; border-radius: 12px; cursor: pointer; transition: all .2s; }
.btn:disabled { opacity: .5; cursor: not-allowed; }
.btn-start { background: linear-gradient(135deg, var(--orange), var(--yellow)); color: #fff; box-shadow: 0 4px 20px rgba(255,126,34,.3); }
.btn-start:hover:not(:disabled) { transform: translateY(-2px); }
.btn-stop { background: #ef4444; color: #fff; box-shadow: 0 4px 20px rgba(239,68,68,.3); }
.btn-stop:hover { transform: translateY(-2px); }
.hint { font-size: 13px; color: var(--text-muted); text-align: center; }
</style>
