<template>
  <div class="container">
    <div class="hero">
      <img src="/logo_baseline.svg" alt="Awabot" class="hero-logo" />
      <h1>Espace Demo</h1>
      <p class="subtitle">Testez les briques IA du projet Awabot en temps reel.</p>
      
      <!-- System Health Monitor -->
      <div class="health-monitor">
        <div class="health-item" v-for="svc in services" :key="svc.name">
          <div class="health-dot" :class="{ 'health-dot--online': svc.online }"></div>
          <span class="health-name">{{ svc.label }}</span>
          <span class="health-status">{{ svc.online ? 'Online' : 'Offline' }}</span>
        </div>
      </div>

      <div class="cards">
        <div v-for="card in cards" :key="card.to" class="demo-card-wrapper">
          <NuxtLink :to="card.to" class="demo-card">
            <div class="demo-header">
              <div :class="['demo-icon', card.iconClass]">{{ card.iconText }}</div>
              <span class="demo-tag">{{ card.tag }}</span>
            </div>
            <h2>{{ card.title }}</h2>
            <p>{{ card.description }}</p>
            
            <div class="model-info">
              <div class="model-name">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                </svg>
                <code>{{ card.model }}</code>
              </div>
              <a :href="card.hfUrl" target="_blank" class="hf-mini-link" @click.stop>
                Hugging Face
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
                  <polyline points="15 3 21 3 21 9"/>
                  <line x1="10" y1="14" x2="21" y2="3"/>
                </svg>
              </a>
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
    tag: 'Mistral AI',
    title: 'Voxtral ASR',
    description: 'Transcription temps reel via Mistral Voxtral Mini 4B.',
    model: 'Voxtral-Mini-4B-Realtime',
    hfUrl: 'https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602'
  },
  {
    to: '/qwen-asr',
    iconClass: 'demo-icon--indigo',
    iconText: 'ASR',
    tag: 'Qwen / Alibaba',
    title: 'Qwen3 ASR',
    description: 'Transcription via Qwen3-ASR 1.7B, optimise pour le multilangue.',
    model: 'Qwen3-ASR-1.7B',
    hfUrl: 'https://huggingface.co/Qwen/Qwen3-ASR-1.7B'
  },
  {
    to: '/qwen-tts',
    iconClass: 'demo-icon--yellow',
    iconText: 'TTS',
    tag: 'Qwen / Alibaba',
    title: 'Qwen3 TTS',
    description: 'Synthese vocale ultra-legere (0.6B) avec clonage de voix.',
    model: 'Qwen3-TTS-0.6B',
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
  max-width: 1000px;
  margin: 0 auto;
  padding: 60px 20px;
}

.hero {
  text-align: center;
}

.hero-logo {
  height: 32px;
  width: auto;
  margin-bottom: 20px;
}

.hero h1 {
  font-size: 42px;
  font-weight: 900;
  letter-spacing: -1.5px;
  color: var(--carbon);
  margin-bottom: 8px;
}

.subtitle {
  color: var(--text-muted);
  font-size: 17px;
  margin-bottom: 32px;
}

/* Health Monitor Styles */
.health-monitor {
  display: inline-flex;
  gap: 32px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 10px 28px;
  border-radius: 50px;
  margin-bottom: 60px;
}

.health-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.health-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #ef4444; /* Offline */
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.08);
  transition: all 0.3s;
}

.health-dot--online {
  background: #10b981;
  box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.08);
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
  font-weight: 700;
  text-transform: uppercase;
  color: var(--text-muted);
}

.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  text-align: left;
}

@media (max-width: 900px) {
  .cards { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 600px) {
  .cards { grid-template-columns: 1fr; }
}

.demo-card {
  display: block;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  text-decoration: none;
  color: var(--text);
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  height: 100%;
}

.demo-card:hover {
  border-color: var(--orange);
  transform: translateY(-4px);
  background: white;
  box-shadow: 0 10px 30px -10px rgba(0,0,0,0.08);
}

.demo-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20px;
}

.demo-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 900;
}

.demo-icon--orange { background: rgba(255, 126, 34, 0.08); color: var(--orange); }
.demo-icon--indigo { background: rgba(99, 102, 241, 0.08); color: #6366f1; }
.demo-icon--yellow { background: rgba(250, 193, 48, 0.1); color: #d97706; }

.demo-card h2 {
  font-size: 18px;
  font-weight: 800;
  margin-bottom: 10px;
  letter-spacing: -0.3px;
}

.demo-card p {
  font-size: 13.5px;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 24px;
}

.demo-tag {
  font-size: 10px;
  font-weight: 700;
  color: var(--text-muted);
  background: var(--bg);
  padding: 4px 10px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.model-info {
  margin-top: auto;
  padding-top: 16px;
  border-top: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.model-name {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  color: var(--text-muted);
}

.model-name code {
  font-family: ui-monospace, monospace;
  background: var(--bg);
  padding: 2px 6px;
  border-radius: 4px;
}

.hf-mini-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 700;
  color: var(--carbon);
  text-decoration: none;
  width: fit-content;
  padding: 4px 0;
  transition: color 0.2s;
}

.hf-mini-link:hover {
  color: var(--orange);
}
</style>
