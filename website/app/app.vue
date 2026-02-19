<template>
  <div class="font-sans text-[#111111] antialiased">
    <NuxtPage />
  </div>
</template>

<style>
@font-face {
  font-family: 'Array';
  src: url('/fonts/Array-Wide.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Switzer';
  src: url('/fonts/Switzer-Regular.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Switzer';
  src: url('/fonts/Switzer-Semibold.woff2') format('woff2');
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}

:root {
  --font-array: 'Array', sans-serif;
  --font-switzer: 'Switzer', sans-serif;
}

body {
  font-family: var(--font-switzer);
}

.font-array {
  font-family: var(--font-array);
}

.font-switzer {
  font-family: var(--font-switzer);
}

.page-enter-active,
.page-leave-active {
  transition: all 0.3s ease-in-out;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(0.5rem);
  transform: translateY(10px);
}

/* Global scrollbar for brand */
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #F5F6F7;
}
::-webkit-scrollbar-thumb {
  background: #FF7E22;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #FAC130;
}

/* Remove ugly glows and set cleaner hovers */
button, a {
  @apply transition-all duration-300;
}

.hover-lift:hover {
  /* Removed scale/translate for a more static premium feel */
  opacity: 0.9;
}
</style>
