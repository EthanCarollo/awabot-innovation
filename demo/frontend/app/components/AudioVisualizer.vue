<template>
  <div class="visualizer">
    <div
      v-for="i in 24"
      :key="i"
      class="bar"
      :style="{ height: `${levels[i - 1] || 4}px`, background: gradient }"
    />
  </div>
</template>

<script setup lang="ts">
defineProps<{
  levels: number[]
  gradient?: string
}>()
</script>

<style scoped>
.visualizer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 3px;
  height: 48px;
}
.bar {
  width: 4px;
  background: linear-gradient(to top, var(--orange), var(--yellow));
  border-radius: 2px;
  transition: height 0.1s;
  min-height: 4px;
}
</style>
