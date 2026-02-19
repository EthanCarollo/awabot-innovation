<template>
  <div id="app">
    <nav class="nav">
      <NuxtLink to="/" class="nav-brand">
        <img src="/logo_baseline.svg" alt="Awabot" class="nav-logo" />
      </NuxtLink>
      <div class="nav-links">
        <NuxtLink to="/voxtral" class="nav-link">Voxtral ASR</NuxtLink>
        <NuxtLink to="/qwen-asr" class="nav-link">Qwen ASR</NuxtLink>
        <NuxtLink to="/qwen-tts" class="nav-link">Qwen TTS</NuxtLink>
      </div>
    </nav>
    <NuxtPage />
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --orange: #FF7E22;
  --yellow: #FAC130;
  --indigo: #6366f1;
  --carbon: #111111;
  --chalk: #F8F9FA;
  --bg: #F8F9FA;
  --bg-card: #ffffff;
  --text: #111111;
  --text-muted: #6B7280;
  --border: #E5E7EB;
  --radius: 20px;
  --radius-sm: 12px;
}

body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-height: 100vh;
}

/* Nav */
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  height: 80px;
  border-bottom: 1px solid var(--border);
  background: rgba(248, 249, 250, 0.8);
  backdrop-filter: blur(12px);
  position: sticky;
  top: 0;
  z-index: 50;
}

.nav-brand {
  text-decoration: none;
  display: flex;
  align-items: center;
}

.nav-logo {
  height: 32px;
  width: auto;
}

.nav-links {
  display: flex;
  gap: 8px;
}

.nav-link {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
  text-decoration: none;
  padding: 10px 18px;
  border-radius: 10px;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.nav-link:hover {
  color: var(--text);
  background: var(--bg-card);
}

.nav-link.router-link-active {
  color: var(--orange);
  background: white;
  border: 1px solid var(--border);
}
</style>
