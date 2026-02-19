// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  app: {
    head: {
      title: 'Awabot Demo — ASR & TTS',
      link: [
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap',
        },
      ],
    },
  },

  runtimeConfig: {
    public: {
      wsBackendBase: process.env.WS_BACKEND_BASE || 'ws://localhost:8080',
    },
  },
})
