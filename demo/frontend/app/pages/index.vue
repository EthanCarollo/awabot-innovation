<template>
  <div class="container">
    <div class="hero">
      <div class="hero-header">
        <img src="/logo_baseline.svg" alt="Awabot" class="hero-logo" />
        <h1>Espace Demo</h1>
        <p class="subtitle">Decouvrez nos briques d'intelligence artificielle souveraines et performantes.</p>
      </div>
      
      <!-- System Health Monitor -->
      <div class="health-monitor">
        <div class="health-item" v-for="svc in services" :key="svc.name">
          <div class="health-dot" :class="{ 'health-dot--online': svc.online }"></div>
          <div class="health-info">
            <span class="health-name">{{ svc.label }}</span>
            <span class="health-status">{{ svc.online ? 'Operationnel' : 'Hors-ligne' }}</span>
          </div>
        </div>
      </div>

      <div class="cards">
        <div v-for="card in cards" :key="card.to" class="demo-card-wrapper">
          <NuxtLink :to="card.to" class="demo-card">
            <div class="card-top">
              <div :class="['demo-icon', card.iconClass]">{{ card.iconText }}</div>
              <span class="demo-tag">{{ card.tag }}</span>
            </div>
            
            <div class="card-body">
              <h2>{{ card.title }}</h2>
              <p>{{ card.description }}</p>
            </div>
            
            <div class="card-footer">
              <div class="model-meta">
                <span class="meta-label">Moteur</span>
                <code class="meta-value">{{ card.model }}</code>
              </div>
              <div class="card-action">
                <span>Tester</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </div>
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const services = ref([
  { name: 'voxtral', label: 'Voxtral ASR', url: 'http://localhost:8082/health', online: false },
  { name: 'qwen-asr', label: 'Qwen ASR', url: 'http://localhost:8083/health', online: false },
  { name: 'qwen-tts', label: 'Qwen TTS', url: 'http://localhost:8084/health', online: false },
])

const cards = [
  {
    to: '/voxtral',
    iconClass: 'demo-icon--orange',
    iconText: 'ASR',
    tag: 'Streaming',
    title: 'Voxtral ASR',
    description: 'Transcription temps reel ultra-rapide basee sur Mistral Voxtral Mini 4B.',
    model: 'Voxtral-4B',
    hfUrl: 'https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602'
  },
  {
    to: '/qwen-asr',
    iconClass: 'demo-icon--indigo',
    iconText: 'ASR',
    tag: 'Multilingue',
    title: 'Qwen3 ASR',
    description: 'Transcription robuste supportant plus de 50 langues avec Qwen3 1.7B.',
    model: 'Qwen3-1.7B',
    hfUrl: 'https://huggingface.co/Qwen/Qwen3-ASR-1.7B'
  },
  {
    to: '/qwen-tts',
    iconClass: 'demo-icon--yellow',
    iconText: 'TTS',
    tag: 'Synthese',
    title: 'Qwen3 TTS',
    description: 'Synthese vocale naturelle et clonage de voix via Qwen3 0.6B.',
    model: 'Qwen3-0.6B',
    hfUrl: 'https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base'
  }
]

let timer: any = null

async function checkHealth() {
  await Promise.all(services.value.map(async (svc) => {
    try {
      const resp = await fetch(svc.url, { mode: 'cors' })
      svc.online = resp.ok
    } catch {
      svc.online = false
    }
  }))
}

onMounted(() => {
  checkHealth()
  timer = setInterval(checkHealth, 5000)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})
</script>

<style scoped>
.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 80px 40px;
}

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.hero-header {
  text-align: center;
  margin-bottom: 48px;
}

.hero-logo {
  height: 36px;
  width: auto;
  margin-bottom: 24px;
}

.hero h1 {
  font-size: 48px;
  font-weight: 900;
  letter-spacing: -2px;
  color: var(--carbon);
  margin-bottom: 12px;
}

.subtitle {
  color: var(--text-muted);
  font-size: 18px;
  max-width: 600px;
  line-height: 1.5;
}

/* Health Monitor Styles */
.health-monitor {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
  margin-bottom: 64px;
}

.health-item {
  display: flex;
  align-items: center;
  gap: 16px;
  background: white;
  padding: 16px 24px;
}

.health-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #EF4444;
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.1);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.health-dot--online {
  background: #10B981;
  box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.1);
}

.health-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.health-name {
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--carbon);
}

.health-status {
  font-size: 10px;
  font-weight: 600;
  color: var(--text-muted);
}

/* Cards */
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  width: 100%;
}

@media (max-width: 960px) {
  .cards { grid-template-columns: repeat(2, 1fr); }
  .health-monitor { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .cards { grid-template-columns: 1fr; }
  .health-monitor { grid-template-columns: 1fr; }
}

.demo-card {
  display: flex;
  flex-direction: column;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 32px;
  text-decoration: none;
  color: var(--text);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  height: 100%;
}

.demo-card:hover {
  border-color: var(--orange);
  transform: translateY(-8px);
  background: white;
}

.card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.demo-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 900;
}

.demo-icon--orange { background: #FF7E2210; color: var(--orange); }
.demo-icon--indigo { background: #6366f110; color: var(--indigo); }
.demo-icon--yellow { background: #FAC13015; color: #D97706; }

.demo-tag {
  font-size: 10px;
  font-weight: 700;
  color: var(--text-muted);
  background: var(--bg);
  padding: 6px 12px;
  border-radius: 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.card-body h2 {
  font-size: 22px;
  font-weight: 800;
  margin-bottom: 12px;
  letter-spacing: -0.5px;
}

.card-body p {
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 32px;
}

.card-footer {
  margin-top: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 24px;
  border-top: 1px solid var(--border);
}

.model-meta {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.meta-label {
  font-size: 9px;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--text-muted);
  letter-spacing: 0.5px;
}

.meta-value {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 11px;
  font-weight: 600;
  color: var(--carbon);
  background: var(--bg);
  padding: 2px 8px;
  border-radius: 6px;
}

.card-action {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 700;
  color: var(--carbon);
  transition: all 0.2s;
}

.demo-card:hover .card-action {
  color: var(--orange);
  transform: translateX(4px);
}
</style>
