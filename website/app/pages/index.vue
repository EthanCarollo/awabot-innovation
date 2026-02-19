<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900">
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_50%,rgba(59,130,246,0.15),transparent_50%)]" />
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_70%_80%,rgba(139,92,246,0.1),transparent_50%)]" />

      <nav class="relative z-10 flex items-center justify-between px-8 py-6 max-w-6xl mx-auto">
        <div class="text-2xl font-extrabold tracking-tight text-white">
          awa<span class="text-blue-400">bot</span>
        </div>
        <div class="flex items-center gap-6">
          <NuxtLink to="/cdc" class="text-sm font-medium text-slate-300 hover:text-white transition-colors">
            Cahier des charges
          </NuxtLink>
        </div>
      </nav>

      <div class="relative z-10 max-w-4xl mx-auto px-8 pt-24 pb-32 text-center">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-300 text-sm font-medium mb-8">
          <span class="w-2 h-2 rounded-full bg-blue-400 animate-pulse" />
          Robotique sociale & IA
        </div>
        <h1 class="text-5xl md:text-6xl font-extrabold text-white leading-tight tracking-tight mb-6">
          L'assistant intelligent
          <span class="bg-gradient-to-r from-blue-400 to-violet-400 bg-clip-text text-transparent">
            au service de l'humain
          </span>
        </h1>
        <p class="text-lg text-slate-400 max-w-2xl mx-auto leading-relaxed mb-10">
          Awabot conçoit des robots compagnons et des solutions d'intelligence artificielle
          pour améliorer le quotidien en entreprise, en santé et en éducation.
        </p>
        <div class="flex items-center justify-center gap-4">
          <NuxtLink
            to="/cdc"
            class="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-blue-500 hover:bg-blue-600 text-white font-semibold text-sm transition-all shadow-lg shadow-blue-500/25 hover:shadow-blue-500/40"
          >
            Voir le cahier des charges →
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="py-24 bg-white">
      <div class="max-w-6xl mx-auto px-8">
        <h2 class="text-3xl font-bold text-slate-900 text-center mb-4">Nos domaines d'expertise</h2>
        <p class="text-slate-500 text-center max-w-xl mx-auto mb-16">
          De la robotique à l'intelligence artificielle, nous développons des solutions innovantes.
        </p>

        <div class="grid md:grid-cols-3 gap-8">
          <div class="group p-8 rounded-2xl border border-slate-200 hover:border-blue-200 hover:shadow-lg hover:shadow-blue-50 transition-all duration-300">
            <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-500 flex items-center justify-center text-2xl mb-5 group-hover:scale-110 transition-transform">
              🤖
            </div>
            <h3 class="text-lg font-bold text-slate-900 mb-2">Robotique sociale</h3>
            <p class="text-sm text-slate-500 leading-relaxed">
              Robots compagnons conçus pour l'interaction humaine, l'assistance et l'accompagnement au quotidien.
            </p>
          </div>

          <div class="group p-8 rounded-2xl border border-slate-200 hover:border-violet-200 hover:shadow-lg hover:shadow-violet-50 transition-all duration-300">
            <div class="w-12 h-12 rounded-xl bg-violet-50 text-violet-500 flex items-center justify-center text-2xl mb-5 group-hover:scale-110 transition-transform">
              🧠
            </div>
            <h3 class="text-lg font-bold text-slate-900 mb-2">Intelligence artificielle</h3>
            <p class="text-sm text-slate-500 leading-relaxed">
              Modèles de reconnaissance vocale et de traitement du langage naturel de pointe.
            </p>
          </div>

          <div class="group p-8 rounded-2xl border border-slate-200 hover:border-emerald-200 hover:shadow-lg hover:shadow-emerald-50 transition-all duration-300">
            <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-500 flex items-center justify-center text-2xl mb-5 group-hover:scale-110 transition-transform">
              💬
            </div>
            <h3 class="text-lg font-bold text-slate-900 mb-2">Interaction vocale</h3>
            <p class="text-sm text-slate-500 leading-relaxed">
              Transcription temps réel et dialogue naturel avec des modèles ASR à faible latence.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-50 border-t border-slate-200 py-10">
      <div class="max-w-6xl mx-auto px-8 flex items-center justify-between">
        <div class="text-sm text-slate-400">
          © {{ new Date().getFullYear() }} Awabot — Tous droits réservés
        </div>
        <NuxtLink to="/cdc" class="text-sm text-slate-400 hover:text-blue-500 transition-colors">
          Cahier des charges
        </NuxtLink>
      </div>
    </footer>
  </div>
</template>
