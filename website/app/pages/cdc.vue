<template>
  <div class="min-h-screen bg-[#F5F6F7]">
    <!-- Mobile TOC Drawer & Overlay -->
    <Transition name="fade">
      <div v-if="isTocOpen" @click="isTocOpen = false" class="fixed inset-0 z-[60] bg-[#111111]/20 lg:hidden backdrop-blur-sm"></div>
    </Transition>

    <div 
      class="fixed inset-y-0 left-0 z-[70] w-72 bg-white shadow-2xl transform transition-transform duration-300 ease-in-out lg:hidden flex flex-col pt-8"
      :class="isTocOpen ? 'translate-x-0' : '-translate-x-full'"
    >
       <div class="px-6 pb-6 overflow-y-auto flex-1 toc-scroll">
         <div class="flex items-center justify-between mb-8 pb-4 border-b border-gray-100">
           <div class="flex items-center gap-2">
             <div class="w-1.5 h-4 bg-awabot-orange rounded-full" />
             <h4 class="text-xs font-bold uppercase tracking-widest text-[#111111]/40">Sommaire</h4>
           </div>
           <button @click="isTocOpen = false" class="text-gray-400 hover:text-gray-800 transition-colors p-2 bg-gray-50 rounded-lg">
             <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
             </svg>
           </button>
         </div>
         <nav v-if="page?.body?.toc?.links" class="space-y-1">
            <template v-for="link in page.body.toc.links" :key="link.id">
              <a
                :href="`#${link.id}`"
                class="block text-[14px] py-3 px-3 rounded-lg text-[#111111]/70 hover:bg-awabot-orange/5 hover:text-awabot-orange transition-colors"
                :class="{ 'text-awabot-orange font-bold bg-awabot-orange/5': activeId === link.id }"
                @click.prevent="scrollTo(link.id)"
              >
                {{ link.text }}
              </a>
              <template v-if="link.children">
                <a
                  v-for="child in link.children"
                  :key="child.id"
                  :href="`#${child.id}`"
                  class="block text-[13px] py-2 px-3 pl-6 rounded-lg text-[#111111]/50 hover:bg-awabot-orange/5 hover:text-awabot-orange transition-colors line-clamp-2"
                  :class="{ 'text-awabot-orange font-semibold bg-awabot-orange/5': activeId === child.id }"
                  @click.prevent="scrollTo(child.id)"
                >
                  {{ child.text }}
                </a>
              </template>
            </template>
         </nav>
       </div>
    </div>

    <!-- Floating TOC Button (Mobile) -->
    <button 
      @click="isTocOpen = true"
      class="lg:hidden fixed bottom-6 left-6 z-[50] w-14 h-14 bg-awabot-orange text-white rounded-full shadow-lg shadow-awabot-orange/30 flex items-center justify-center hover:scale-105 transition-all active:scale-95"
      :class="{ 'translate-y-24 opacity-0 pointer-events-none': isTocOpen }"
      aria-label="Ouvrir le sommaire"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>
    </button>

    <!-- Top bar -->
    <header class="sticky top-0 z-50 bg-[#F5F6F7]/90 backdrop-blur-md border-b border-gray-200 h-20">
      <nav class="max-w-[1700px] mx-auto px-6 md:px-12 lg:px-20 h-full flex items-center justify-between relative">
        <!-- Logo -->
        <div class="flex items-center">
          <NuxtLink to="/" class="cursor-pointer">
            <img src="/logo_baseline.svg" alt="Awabot" class="h-8 md:h-10 lg:h-12 w-auto" />
          </NuxtLink>
        </div>
        
        <!-- Breadcrumb / Links -->
        <div class="flex items-center gap-3 sm:gap-4">
          <NuxtLink to="/" class="text-[11px] sm:text-[13px] font-bold uppercase tracking-wider text-[#111111]/40 hover:text-awabot-orange transition-colors">Accueil</NuxtLink>
          <div class="w-px h-4 bg-gray-300" />
          <span class="text-[11px] sm:text-[13px] font-bold uppercase tracking-wider text-awabot-orange">Cahier des charges</span>
        </div>
      </nav>
    </header>

    <div class="max-w-7xl mx-auto flex flex-col lg:flex-row gap-6 lg:gap-12 px-4 sm:px-6 py-6 sm:py-8 lg:py-12">
      <!-- Sidebar TOC -->
      <aside class="hidden lg:block w-56 shrink-0">
        <div class="sticky top-24">
          <div class="flex items-center gap-2 mb-6 ml-4">
            <div class="w-1 h-3 bg-awabot-orange rounded-full" />
            <h4 class="text-[10px] font-bold uppercase tracking-widest text-[#111111]/40">Sommaire</h4>
          </div>
          <nav v-if="page?.body?.toc?.links" class="space-y-0.5 max-h-[calc(100vh-10rem)] overflow-y-auto toc-scroll">
            <template v-for="link in page.body.toc.links" :key="link.id">
              <a
                :href="`#${link.id}`"
                class="group block text-[13px] py-1.5 px-4 rounded-r-lg transition-all duration-200 border-l-2"
                :class="activeId === link.id
                  ? 'text-awabot-orange font-bold border-awabot-orange bg-awabot-orange/5'
                  : 'text-[#111111]/50 border-transparent hover:text-awabot-orange hover:border-awabot-orange/20'"
                @click.prevent="scrollTo(link.id)"
              >
                {{ link.text }}
              </a>
              <template v-if="link.children">
                <a
                  v-for="child in link.children"
                  :key="child.id"
                  :href="`#${child.id}`"
                  class="block text-[12px] py-1 px-4 pl-8 rounded-r-lg transition-all duration-200 border-l-2"
                  :class="activeId === child.id
                    ? 'text-awabot-orange/80 font-bold border-awabot-orange/40 bg-awabot-orange/5'
                    : 'text-[#111111]/40 border-transparent hover:text-awabot-orange/70 hover:border-awabot-orange/10'"
                  @click.prevent="scrollTo(child.id)"
                >
                  {{ child.text }}
                </a>
              </template>
            </template>
          </nav>
        </div>
      </aside>

      <!-- Document -->
      <main class="flex-1 min-w-0">
        <article class="bg-white rounded-2xl sm:rounded-[32px] border border-gray-100 p-6 sm:p-10 md:p-16 lg:p-20 prose prose-slate prose-base sm:prose-lg max-w-none
          prose-headings:font-black prose-headings:tracking-tight prose-headings:text-[#111111]
          
          prose-h1:text-3xl sm:prose-h1:text-4xl prose-h1:mb-8 sm:prose-h1:mb-12 prose-h1:pb-4 sm:prose-h1:pb-6 prose-h1:border-b-4 prose-h1:border-awabot-orange
          
          prose-h2:text-xl sm:prose-h2:text-2xl prose-h2:mt-12 sm:prose-h2:mt-20 prose-h2:mb-6 sm:prose-h2:mb-8 prose-h2:flex prose-h2:items-center prose-h2:gap-2 sm:prose-h2:gap-3
          prose-h2:before:content-[''] prose-h2:before:w-1.5 sm:prose-h2:before:w-2 prose-h2:before:h-6 sm:prose-h2:before:h-8 prose-h2:before:bg-awabot-orange prose-h2:before:rounded-full
          prose-h2:border-none
          
          prose-h3:text-lg sm:prose-h3:text-xl prose-h3:mt-8 sm:prose-h3:mt-12 prose-h3:text-awabot-orange/90 prose-h3:font-extrabold
          
          prose-p:text-[#111111]/70 prose-p:leading-[1.7] sm:prose-p:leading-[1.8] prose-p:text-[15px] sm:prose-p:text-[17px]
          
          prose-li:text-[#111111]/70 prose-li:marker:text-awabot-orange prose-li:my-1 prose-li:text-[15px] sm:prose-li:text-[17px]
          
          prose-strong:text-[#111111] prose-strong:font-bold
          
          prose-a:text-awabot-orange prose-a:font-semibold prose-a:decoration-2 prose-a:underline-offset-4 hover:prose-a:text-awabot-yellow transition-colors break-words
          
          prose-code:text-awabot-orange prose-code:bg-awabot-orange/5 prose-code:px-1.5 sm:prose-code:px-2 prose-code:py-0.5 prose-code:rounded-md sm:prose-code:rounded-lg prose-code:font-bold prose-code:text-[0.85em] sm:prose-code:text-[0.9em] prose-code:before:content-none prose-code:after:content-none prose-code:break-words
          
          prose-blockquote:border-l-4 prose-blockquote:border-awabot-yellow prose-blockquote:bg-awabot-yellow/5 prose-blockquote:py-2 prose-blockquote:px-5 sm:prose-blockquote:px-8 prose-blockquote:rounded-r-xl sm:prose-blockquote:rounded-r-2xl prose-blockquote:italic prose-blockquote:text-[#111111]/80 prose-blockquote:before:content-none prose-blockquote:after:content-none prose-blockquote:text-[15px] sm:prose-blockquote:text-[17px]
          
          prose-table:text-[13px] sm:prose-table:text-[15px] prose-table:border-collapse prose-table:my-8 sm:prose-table:my-10 prose-table:block prose-table:overflow-x-auto prose-table:w-full
          prose-th:bg-[#F5F6F7] prose-th:text-[#111111] prose-th:p-3 sm:prose-th:p-4 prose-th:font-bold prose-th:border prose-th:border-gray-200 prose-th:whitespace-nowrap
          prose-td:p-3 sm:prose-td:p-4 prose-td:border prose-td:border-gray-100 prose-td:text-gray-600
          
          prose-img:my-8 sm:prose-img:my-12 prose-img:mx-auto prose-img:rounded-lg
          
          prose-hr:my-10 sm:prose-hr:my-16 prose-hr:border-gray-100
        ">
          <ContentRenderer v-if="page" :value="page" />
        </article>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'

const isTocOpen = ref(false)

// Prevent body scroll when TOC is open on mobile
watch(isTocOpen, (val) => {
  if (typeof window !== 'undefined') {
    document.body.style.overflow = val ? 'hidden' : ''
  }
})

useHead({ 
  title: 'Cahier des Charges — Awabot',
  meta: [
    { name: 'description', content: 'Cahier des charges technique et fonctionnel pour le projet de modernisation Nuxt.js d\'Awabot.' }
  ]
})

const { data: page } = await useAsyncData('cdc', () =>
  queryCollection('content').path('/cdc').first()
)

const activeId = ref('')

function scrollTo(id: string) {
  const el = document.getElementById(id)
  if (el) {
    const yOffset = -100
    const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset
    window.scrollTo({ top: y, behavior: 'smooth' })
    activeId.value = id
    isTocOpen.value = false
  }
}

let observer: IntersectionObserver | null = null

onMounted(() => {
  const headings = document.querySelectorAll('article h1[id], article h2[id], article h3[id]')

  observer = new IntersectionObserver(
    (entries) => {
      // Find the first entry that is intersecting
      const visible = entries.find(e => e.isIntersecting)
      if (visible) {
        activeId.value = visible.target.id
      }
    },
    { 
      rootMargin: '-10% 0px -80% 0px', // Trigger when heading is near top
      threshold: 0 
    }
  )

  headings.forEach((h) => observer!.observe(h))

  // Initial active state based on hash
  if (window.location.hash) {
    activeId.value = window.location.hash.slice(1)
  }
})

onUnmounted(() => {
  observer?.disconnect()
})
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.toc-scroll::-webkit-scrollbar {
  width: 4px;
}
.toc-scroll::-webkit-scrollbar-track {
  background: transparent;
}
.toc-scroll::-webkit-scrollbar-thumb {
  background: #FF7E22;
  border-radius: 99px;
  opacity: 0.2;
}

@media print {
  nav, aside { display: none !important; }
  .min-h-screen { background: white !important; }

  article {
    box-shadow: none !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
    font-size: 12pt;
  }

  main {
    padding: 0 !important;
    max-width: 100% !important;
  }

  h1, h2, h3 { page-break-after: avoid; }
  pre, blockquote, img { page-break-inside: avoid; }
}
</style>
