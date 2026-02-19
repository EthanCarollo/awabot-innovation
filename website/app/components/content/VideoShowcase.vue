<template>
  <div class="video-showcase-container my-12">
    <div class="video-wrapper overflow-hidden rounded-2xl border border-white/10 bg-black/20 backdrop-blur-sm">
      <video
        ref="videoEl"
        :src="src"
        class="w-full aspect-video object-cover"
        controls
        preload="none"
        playsinline
      ></video>
      <div v-if="caption" class="caption-bar px-2 py-0.5 bg-white/5 border-t border-white/10 text-center">
        <p class="text-[10px] font-medium text-white/30 italic leading-tight">{{ caption }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  src: string
  caption?: string
}>()
</script>
