<template>
  <div class="min-h-screen bg-[#F5F6F7]">
    <!-- Top bar -->
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <NuxtLink to="/" class="text-lg font-extrabold tracking-tight text-[#111111]">
          awa<span class="text-awabot-orange">bot</span>
        </NuxtLink>
        <span class="text-sm font-medium text-gray-400">Cahier des charges</span>
      </div>
    </nav>

    <div class="max-w-7xl mx-auto flex gap-8 px-6 py-12">
      <!-- Sidebar TOC -->
      <aside class="hidden lg:block w-64 shrink-0">
        <div class="sticky top-24">
          <h4 class="text-xs font-bold uppercase tracking-widest text-awabot-orange mb-4">Sommaire</h4>
          <nav v-if="page?.body?.toc?.links" class="space-y-1 max-h-[calc(100vh-8rem)] overflow-y-auto pr-2 toc-scroll">
            <template v-for="link in page.body.toc.links" :key="link.id">
              <a
                :href="`#${link.id}`"
                class="block text-sm py-1.5 px-3 rounded-lg transition-all duration-200 hover:bg-awabot-orange/5"
                :class="activeId === link.id
                  ? 'text-awabot-orange font-semibold bg-awabot-orange/10 border-l-2 border-awabot-orange'
                  : 'text-[#111111]/60 hover:text-[#111111]'"
                @click.prevent="scrollTo(link.id)"
              >
                {{ link.text }}
              </a>
              <template v-if="link.children">
                <a
                  v-for="child in link.children"
                  :key="child.id"
                  :href="`#${child.id}`"
                  class="block text-xs py-1 px-3 pl-6 rounded-lg transition-all duration-200 hover:bg-awabot-yellow/5"
                  :class="activeId === child.id
                    ? 'text-awabot-yellow font-semibold bg-awabot-yellow/10 border-l-2 border-awabot-yellow'
                    : 'text-[#111111]/40 hover:text-[#111111]/70'"
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
        <article class="bg-white rounded-2xl shadow-sm border border-gray-200 p-10 md:p-16 prose prose-lg max-w-none
          prose-headings:font-bold prose-headings:tracking-tight prose-headings:text-[#111111]
          prose-h1:text-3xl prose-h1:pb-4 prose-h1:border-b-2 prose-h1:border-awabot-orange
          prose-h2:text-xl prose-h2:mt-12 prose-h2:pb-2 prose-h2:border-b prose-h2:border-gray-200
          prose-h3:text-lg
          prose-p:text-[#111111]/75 prose-p:leading-relaxed
          prose-li:text-[#111111]/75 prose-li:marker:text-awabot-orange
          prose-strong:text-[#111111]
          prose-a:text-awabot-orange prose-a:no-underline hover:prose-a:underline
          prose-code:text-awabot-orange prose-code:bg-awabot-orange/5 prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded prose-code:text-sm prose-code:before:content-none prose-code:after:content-none
          prose-blockquote:border-awabot-yellow prose-blockquote:bg-awabot-yellow/5 prose-blockquote:rounded-r-xl prose-blockquote:text-[#111111]
          prose-table:text-sm
          prose-th:bg-[#F5F6F7] prose-th:text-[#111111]
          prose-td:border-gray-200
          prose-img:rounded-xl prose-img:shadow-sm
          prose-hr:border-gray-200
        ">
          <ContentRenderer v-if="page" :value="page" />
        </article>

        <div class="text-center py-10 text-sm text-gray-400">
          Awabot — Cahier des Charges · {{ new Date().getFullYear() }}
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

useHead({ title: 'Cahier des Charges — Awabot' })

const { data: page } = await useAsyncData('cdc', () =>
  queryCollection('content').path('/cdc').first()
)

const activeId = ref('')

function scrollTo(id: string) {
  const el = document.getElementById(id)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' })
    activeId.value = id
  }
}

let observer: IntersectionObserver | null = null

onMounted(() => {
  const headings = document.querySelectorAll('article h1[id], article h2[id], article h3[id]')

  observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          activeId.value = entry.target.id
          break
        }
      }
    },
    { rootMargin: '-80px 0px -70% 0px', threshold: 0.1 }
  )

  headings.forEach((h) => observer!.observe(h))
})

onUnmounted(() => {
  observer?.disconnect()
})
</script>

<style>
.toc-scroll::-webkit-scrollbar {
  width: 3px;
}
.toc-scroll::-webkit-scrollbar-track {
  background: transparent;
}
.toc-scroll::-webkit-scrollbar-thumb {
  background: #FF7E22;
  border-radius: 99px;
  opacity: 0.3;
}

@media print {
  nav, aside { display: none !important; }
  .min-h-screen { background: white !important; }

  article {
    box-shadow: none !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
  }

  main {
    padding: 0 !important;
    max-width: 100% !important;
  }
}
</style>
