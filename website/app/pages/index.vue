<template>
  <div class="min-h-screen bg-white selection:bg-awabot-orange/20">
    <!-- Header -->
    <header class="relative z-50 flex items-center justify-between px-8 md:px-16 py-8">
      <nav class="hidden md:flex items-center gap-12">
        <NuxtLink to="/" class="text-[17px] font-medium text-slate-800 hover:text-awabot-orange transition-colors">
          {{ t.nav.about }}
        </NuxtLink>
        <NuxtLink to="/" class="text-[17px] font-medium text-slate-800 hover:text-awabot-orange transition-colors">
          {{ t.nav.usage }}
        </NuxtLink>
      </nav>

      <div class="md:absolute md:left-1/2 md:-translate-x-1/2">
        <img src="/logo_baseline.svg" alt="Awabot" class="h-12 w-auto" />
      </div>

      <nav class="hidden md:flex items-center gap-12">
        <NuxtLink to="/" class="text-[17px] font-medium text-slate-800 hover:text-awabot-orange transition-colors">
          {{ t.nav.robots }}
        </NuxtLink>
        <NuxtLink to="/" class="text-[17px] font-medium text-slate-800 hover:text-awabot-orange transition-colors">
          {{ t.nav.quote }}
        </NuxtLink>
        <div class="flex items-center gap-1.5 text-[15px] font-medium">
          <button 
            @click="lang = 'fr'" 
            :class="lang === 'fr' ? 'text-awabot-orange' : 'text-slate-800 opacity-60 hover:opacity-100'"
            class="transition-all"
          >Fr</button>
          <span class="text-slate-300">|</span>
          <button 
            @click="lang = 'en'" 
            :class="lang === 'en' ? 'text-awabot-orange' : 'text-slate-800 opacity-60 hover:opacity-100'"
            class="transition-all"
          >En</button>
        </div>
      </nav>
      
      <!-- Mobile menu button -->
      <button class="md:hidden text-slate-800">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    </header>

    <main class="relative">
      <!-- Hero Section -->
      <div class="max-w-[1700px] ml-auto overflow-hidden">
        <div class="flex flex-col lg:flex-row items-center">
          <div class="w-full lg:w-[48%] px-8 md:pl-16 lg:pl-24 py-12 lg:py-24">
            <h1 class="text-[44px] md:text-[58px] lg:text-[76px] font-bold leading-[1.05] tracking-tight text-slate-900 mb-14">
              <span class="text-awabot-orange">Awabot</span> {{ t.hero.title }}
            </h1>
            
            <NuxtLink
              to="/"
              class="group inline-flex items-center gap-6 bg-awabot-yellow hover:bg-[#F9B520] pl-10 pr-3 py-3 rounded-full text-[18px] font-bold text-slate-900 transition-all shadow-sm hover:shadow-md active:scale-95"
            >
              {{ t.nav.quote }}
              <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-sm transition-transform group-hover:translate-x-1">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="text-awabot-yellow"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </div>
            </NuxtLink>
          </div>

          <div class="w-full lg:w-[52%] flex justify-end">
            <div class="relative w-full h-[500px] md:h-[600px] lg:h-[680px] overflow-hidden rounded-l-[180px] md:rounded-l-[280px] lg:rounded-l-[380px] shadow-xl">
              <img 
                src="/hero-robot.png" 
                alt="Beam Robot" 
                class="absolute inset-0 w-full h-full object-cover object-center"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- Feature Section 1: Beam & BeamPro -->
      <section class="py-32 px-8 overflow-hidden">
        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row items-center gap-20">
          <div class="w-full lg:w-1/2">
            <p class="text-awabot-orange font-bold uppercase tracking-widest text-sm mb-6">{{ t.features.beam.label }}</p>
            <h2 class="text-4xl md:text-5xl font-bold text-slate-900 mb-8 leading-tight">
              {{ t.features.beam.title }}
            </h2>
            <p class="text-[19px] text-slate-600 leading-relaxed mb-10 max-w-xl">
              {{ t.features.beam.desc }}
            </p>
            <div class="flex flex-wrap gap-4">
              <button class="bg-slate-800 text-white px-8 py-3 rounded-full font-bold hover:bg-slate-700 transition-all">{{ t.btns.more }}</button>
              <button class="border-2 border-slate-800 text-slate-800 px-8 py-3 rounded-full font-bold hover:bg-slate-50 transition-all">{{ t.btns.contact }}</button>
            </div>
          </div>
          <div class="w-full lg:w-1/2 relative">
            <div class="relative w-full aspect-[4/3] rounded-[60px] overflow-hidden bg-slate-50 flex items-center justify-center border border-slate-100">
               <!-- Product Image Placeholder -->
               <img src="/hero-robot.png" alt="Beam Robots" class="w-full h-full object-contain p-12" />
            </div>
          </div>
        </div>
      </section>

      <!-- Feature Section 2: Education -->
      <section class="py-32 px-8 bg-slate-50">
        <div class="max-w-7xl mx-auto flex flex-col-reverse lg:flex-row items-center gap-20">
          <div class="w-full lg:w-1/2 relative">
            <div class="relative w-full aspect-[4/3] rounded-[60px] overflow-hidden shadow-2xl">
               <!-- Classroom Image Placeholder -->
               <img src="/voxtral_benchmark.png" alt="Education" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="w-full lg:w-1/2">
            <p class="text-awabot-orange font-bold uppercase tracking-widest text-sm mb-6">{{ t.features.edu.label }}</p>
            <h2 class="text-4xl md:text-5xl font-bold text-slate-900 mb-8 leading-tight">
              {{ t.features.edu.title }}
            </h2>
            <p class="text-[19px] text-slate-600 leading-relaxed mb-10">
              {{ t.features.edu.desc }}
            </p>
            <div class="flex flex-wrap gap-4">
              <button class="bg-awabot-orange text-white px-8 py-3 rounded-full font-bold hover:shadow-lg hover:shadow-awabot-orange/30 transition-all">{{ t.btns.more }}</button>
              <button class="bg-white border-2 border-awabot-orange text-awabot-orange px-8 py-3 rounded-full font-bold hover:bg-orange-50 transition-all">{{ t.btns.contact }}</button>
            </div>
          </div>
        </div>
      </section>
      <!-- News Section: Full Width & Overlay Style -->
      <section class="py-24 bg-white overflow-hidden">
        <div class="px-8 md:px-16 mb-16 flex flex-col md:flex-row md:items-end justify-between gap-8">
          <div>
            <p class="text-awabot-orange font-bold text-sm mb-3 uppercase tracking-widest">{{ t.news.label }}</p>
            <h2 class="text-4xl md:text-5xl lg:text-6xl font-black text-slate-900 tracking-tight">{{ t.news.title }}</h2>
          </div>
          <button class="flex items-center gap-4 bg-[#E32342] hover:bg-[#C11B35] text-white px-10 py-4 rounded-full font-bold transition-all group shrink-0 shadow-lg shadow-red-500/20">
            {{ t.news.allArticles }}
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="transition-transform group-hover:translate-x-1"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>
        </div>

        <!-- Full Width Masonry-ish Grid -->
        <div class="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-4 h-auto md:h-[900px]">
          <!-- Big Item 1 -->
          <div class="md:col-span-2 md:row-span-2 group relative overflow-hidden cursor-pointer border-r border-b border-white lg:border-none">
            <img src="/hero-robot.png" alt="F1 News" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent p-10 flex flex-col justify-end">
              <span class="text-awabot-yellow font-bold text-sm uppercase tracking-widest mb-4">Formule 1</span>
              <h3 class="text-3xl md:text-4xl font-extrabold text-white leading-[1.1] mb-8 max-w-xl">
                {{ t.news.items[0] }}
              </h3>
              <div class="flex">
                <span class="inline-flex items-center gap-3 text-white font-bold text-lg group/btn">
                  {{ t.btns.more }}
                  <div class="w-10 h-10 rounded-full border-2 border-white/30 flex items-center justify-center transition-all group-hover/btn:bg-white group-hover/btn:border-white">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="transition-colors group-hover/btn:text-slate-900"><polyline points="9 18 15 12 9 6"></polyline></svg>
                  </div>
                </span>
              </div>
            </div>
          </div>

          <!-- Item 2 -->
          <div class="md:col-span-1 group relative overflow-hidden cursor-pointer border-r border-b border-white lg:border-none">
            <img src="/voxtral_benchmark.png" alt="TED-i" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent p-8 flex flex-col justify-end">
              <span class="text-awabot-yellow font-bold text-xs uppercase tracking-widest mb-3">Éducation</span>
              <h3 class="text-xl font-bold text-white leading-tight mb-6">
                {{ t.news.items[1] }}
              </h3>
              <span class="text-white/70 font-bold text-sm uppercase tracking-widest flex items-center gap-2">
                Lire la suite <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </span>
            </div>
          </div>

          <!-- Item 3 -->
          <div class="md:col-span-1 group relative overflow-hidden cursor-pointer border-b border-white lg:border-none">
            <img src="/hero-robot.png" alt="Flexi Beam" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent p-8 flex flex-col justify-end">
              <span class="text-awabot-yellow font-bold text-xs uppercase tracking-widest mb-3">Location</span>
              <h3 class="text-xl font-bold text-white leading-tight mb-6">
                {{ t.news.items[2] }}
              </h3>
              <span class="text-white/70 font-bold text-sm uppercase tracking-widest flex items-center gap-2">
                Lire la suite <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </span>
            </div>
          </div>

          <!-- Item 4 -->
          <div class="md:col-span-1 group relative overflow-hidden cursor-pointer border-r border-white lg:border-none">
            <img src="/voxtral_benchmark.png" alt="Olympics" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent p-8 flex flex-col justify-end">
              <span class="text-awabot-yellow font-bold text-xs uppercase tracking-widest mb-3">Événement</span>
              <h3 class="text-lg font-bold text-white leading-tight mb-6">
                {{ t.news.items[3] }}
              </h3>
              <span class="text-white/70 font-bold text-sm uppercase tracking-widest flex items-center gap-2">
                Lire la suite <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </span>
            </div>
          </div>

          <!-- Item 5 -->
          <div class="md:col-span-1 group relative overflow-hidden cursor-pointer lg:border-none">
            <img src="/hero-robot.png" alt="HIKU" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent p-8 flex flex-col justify-end">
              <span class="text-awabot-yellow font-bold text-xs uppercase tracking-widest mb-3">Innovation</span>
              <h3 class="text-lg font-bold text-white leading-tight mb-6">
                {{ t.news.items[4] }}
              </h3>
              <span class="text-white/70 font-bold text-sm uppercase tracking-widest flex items-center gap-2">
                Lire la suite <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </span>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- Bottom Orange Accent Bar -->
    <footer class="w-full h-48 bg-awabot-orange flex flex-col items-center justify-center gap-4">
      <div class="flex gap-8 mb-4">
        <NuxtLink to="/" class="text-white/80 hover:text-white font-medium transition-colors">{{ t.nav.about }}</NuxtLink>
        <NuxtLink to="/" class="text-white/80 hover:text-white font-medium transition-colors">{{ t.nav.usage }}</NuxtLink>
        <NuxtLink to="/" class="text-white/80 hover:text-white font-medium transition-colors">{{ t.nav.robots }}</NuxtLink>
      </div>
      <p class="text-white/60 font-medium">© {{ new Date().getFullYear() }} Awabot — Tous droits réservés</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const lang = ref('fr')

const translations = {
  fr: {
    nav: {
      about: 'À propos',
      usage: 'Usages',
      robots: 'Robots Beam®',
      quote: 'Demander un devis'
    },
    hero: {
      title: "l'outil de téléprésence qui vous réunit depuis plus de 10 ans"
    },
    features: {
      beam: {
        label: 'Robots de téléprésence Beam® et BeamPro®',
        title: 'Présent, même à distance !',
        desc: "Beam® compense la distance et restitue l'interaction sociale au plus proche du réel. À l'école, en entreprise ou dans un lieu public, il devient votre avatar."
      },
      edu: {
        label: "À propos d'Awabot",
        title: 'Experts de la Téléprésence au service du lien Humain',
        desc: "Depuis plus de 10 ans, Awabot est pionnier dans le domaine de la téléprésence robotique. L'entreprise est particulièrement engagée à rompre l'isolement social."
      }
    },
    news: {
      label: 'À la une',
      title: "L'actualité d'Awabot",
      allArticles: 'Tous les articles',
      items: [
        "Fin de saison Formule 1 : l'inclusion en pole position",
        "TED-i : Une cartographie interactive pour suivre les déploiements",
        "Flexi' Beam® : le robot de téléprésence disponible en location",
        "Jeux Olympiques et Paralympiques : l'engagement d'Awabot",
        "HIKU : la nouvelle expérience de téléprésence"
      ]
    },
    btns: {
      more: 'En savoir plus',
      contact: 'Nous contacter'
    }
  },
  en: {
    nav: {
      about: 'About',
      usage: 'Usage',
      robots: 'Beam® Robots',
      quote: 'Request a Quote'
    },
    hero: {
      title: "the telepresence tool that has been reuniting you for over 10 years"
    },
    features: {
      beam: {
        label: 'Telepresence Robots Beam® and BeamPro®',
        title: 'Present, even from a distance!',
        desc: "Beam® compensates for distance and restores social interaction as close to reality as possible. At school, in business or in a public place, it becomes your avatar."
      },
      edu: {
        label: 'About Awabot',
        title: 'Telepresence Experts at the service of human connection',
        desc: "For over 10 years, Awabot has been a pioneer in the field of robotic telepresence. The company is particularly committed to breaking social isolation."
      }
    },
    news: {
      label: 'Featured',
      title: 'Awabot News',
      allArticles: 'All articles',
      items: [
        "Formula 1 season finale: inclusion in pole position",
        "TED-i: An interactive map to track deployments",
        "Flexi' Beam®: the telepresence robot available for rent",
        "Olympic and Paralympic Games: Awabot's commitment",
        "HIKU: the new telepresence experience"
      ]
    },
    btns: {
      more: 'Learn more',
      contact: 'Contact us'
    }
  }
}

const t = computed(() => translations[lang.value])
</script>

<style scoped>
/* Smooth transition for language switch */
.transition-all {
  transition: all 0.2s ease-in-out;
}
</style>

