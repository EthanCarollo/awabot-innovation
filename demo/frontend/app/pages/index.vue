<template>
  <div class="container">
    <div class="hero">
      <img src="/logo_baseline.svg" alt="Awabot" class="hero-logo" />
      <h1>Espace Demo</h1>
      <p class="subtitle">Testez les briques IA du projet Awabot en temps reel.</p>
      <div class="cards">
        <NuxtLink to="/voxtral" class="demo-card">
          <div class="demo-icon demo-icon--orange">ASR</div>
          <h2>Voxtral ASR</h2>
          <p>Transcription temps reel via Mistral Voxtral Mini 4B.</p>
          <span class="demo-tag">Mistral AI</span>
        </NuxtLink>
        <NuxtLink to="/qwen-asr" class="demo-card">
          <div class="demo-icon demo-icon--indigo">ASR</div>
          <h2>Qwen3 ASR</h2>
          <p>Transcription via Qwen3-ASR 1.7B, optimise pour le multilangue.</p>
          <span class="demo-tag">Qwen / Alibaba</span>
        </NuxtLink>
        <NuxtLink to="/qwen-tts" class="demo-card">
          <div class="demo-icon demo-icon--yellow">TTS</div>
          <h2>Qwen3 TTS</h2>
          <p>Synthese vocale ultra-legere (0.6B) avec clonage de voix.</p>
          <span class="demo-tag">Qwen / Alibaba</span>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 80px 20px;
}

.hero {
  text-align: center;
}

.hero-logo {
  height: 40px;
  width: auto;
  margin-bottom: 24px;
}

.hero h1 {
  font-size: 36px;
  font-weight: 900;
  letter-spacing: -1px;
  color: var(--carbon);
  margin-bottom: 8px;
}

.subtitle {
  color: var(--text-muted);
  font-size: 16px;
  margin-bottom: 48px;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  text-align: left;
}

.demo-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  text-decoration: none;
  color: var(--text);
  transition: all 0.2s;

}

.demo-card:hover {
  border-color: var(--orange);
  transform: translateY(-2px);
}

.demo-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 800;
  margin-bottom: 16px;
}

.demo-icon--orange { background: rgba(255, 126, 34, 0.1); color: var(--orange); }
.demo-icon--indigo { background: rgba(99, 102, 241, 0.1); color: #6366f1; }
.demo-icon--yellow { background: rgba(250, 193, 48, 0.15); color: #d97706; }

.demo-card h2 {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 6px;
}

.demo-card p {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.5;
  margin-bottom: 16px;
}

.demo-tag {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-muted);
  background: var(--bg);
  padding: 4px 10px;
  border-radius: 6px;
}
</style>
