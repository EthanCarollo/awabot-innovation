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
  --carbon: #111111;
  --chalk: #F5F6F7;
  --bg: #F5F6F7;
  --bg-card: #ffffff;
  --bg-card-hover: #fafafa;
  --text: #111111;
  --text-muted: #111111a0;
  --border: #11111115;
  --radius: 16px;
}

body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
}

/* Nav */
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  height: 72px;
  border-bottom: 1px solid var(--border);
  background: var(--bg);
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
  height: 28px;
  width: auto;
}

.nav-links {
  display: flex;
  gap: 4px;
}

.nav-link {
  font-size: 14px;
  font-weight: 700;
  color: var(--text-muted);
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 8px;
  transition: all 0.2s;
}

.nav-link:hover {
  color: var(--text);
  background: var(--border);
}

.nav-link.router-link-active {
  color: var(--orange);
  background: rgba(255, 126, 34, 0.08);
}
</style>
