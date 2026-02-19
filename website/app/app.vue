<template>
  <div class="font-sans text-[#111111] antialiased">
    <NuxtPage />
  </div>
</template>

<style>
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
</style>
