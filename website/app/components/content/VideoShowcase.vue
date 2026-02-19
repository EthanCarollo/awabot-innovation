<template>
  <div class="video-showcase-container my-12">
    <div class="video-wrapper overflow-hidden rounded-2xl border border-white/10 bg-black/20 shadow-2xl backdrop-blur-sm">
      <video
        ref="videoEl"
        :src="src"
        class="w-full aspect-video object-cover"
        controls
        muted
        playsinline
        loop
      ></video>
      <div v-if="caption" class="caption-bar p-4 bg-white/5 border-t border-white/10 text-center">
        <p class="text-sm font-medium text-white/70 italic">{{ caption }}</p>
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

<style scoped>
.video-showcase-container {
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.video-wrapper {
  transition: transform 0.3s ease;
}

.video-wrapper:hover {
  transform: translateY(-4px);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}
</style>
