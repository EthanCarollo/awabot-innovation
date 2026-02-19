<template>
  <div class="min-h-screen bg-[#F5F6F7] selection:bg-awabot-orange/20">
    <!-- Navigation -->
    <header class="fixed top-0 left-0 right-0 z-50 bg-[#F5F6F7] border-b border-awabot-carbon/10 h-20">
      <nav class="max-w-[1700px] mx-auto px-12 md:px-20 h-full flex items-center justify-between relative">
        <!-- Left: Desktop Nav Links -->
        <div class="hidden lg:flex items-center gap-6">
          <a href="#" class="text-[15px] font-bold text-awabot-carbon transition-colors hover:text-awabot-orange whitespace-nowrap">{{ t.nav.about }}</a>
          <a href="#" class="text-[15px] font-bold text-awabot-carbon transition-colors hover:text-awabot-orange whitespace-nowrap">{{ t.nav.robots }}</a>
          <a href="#" class="text-[15px] font-bold text-awabot-carbon transition-colors hover:text-awabot-orange whitespace-nowrap">{{ t.nav.usage }}</a>
          <a href="#" class="text-[15px] font-bold text-awabot-carbon transition-colors hover:text-awabot-orange whitespace-nowrap">{{ t.nav.news }}</a>
        </div>

        <!-- Center: Logo -->
        <div class="flex items-center pointer-events-none lg:absolute lg:inset-0 lg:justify-center">
          <a href="/" class="pointer-events-auto cursor-pointer">
            <img src="/logo_baseline.svg" alt="Awabot" class="h-10 lg:h-14 w-auto" />
          </a>
        </div>

        <!-- Right: Actions -->
        <div class="flex items-center gap-4">
          <!-- Desktop Secondary Nav -->
          <div class="hidden 2xl:flex items-center gap-6 border-r border-awabot-carbon/10 pr-6 mr-2">
            <a href="#" class="flex items-center gap-2 text-[13px] font-bold text-awabot-carbon/60 hover:text-awabot-carbon transition-colors whitespace-nowrap">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 1 1-7.6-12.7 8.35 8.35 0 0 1 4.3 1.25L21 3v8.5z"></path></svg>
              {{ t.nav.help }}
            </a>
            <a href="#" class="flex items-center gap-2 text-[13px] font-bold text-awabot-carbon/60 hover:text-awabot-carbon transition-colors whitespace-nowrap">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
              {{ t.nav.manage }}
            </a>
          </div>

          <div class="flex items-center gap-2.5 text-[13px] mr-6">
            <button @click="lang = 'fr'" :class="lang === 'fr' ? 'text-[#ff7e22] font-bold' : 'text-[#111111]/40 font-medium hover:text-[#ff7e22] transition-colors'">Fr</button>
            <span class="text-[#111111]/10">|</span>
            <button @click="lang = 'en'" :class="lang === 'en' ? 'text-[#ff7e22] font-bold' : 'text-[#111111]/40 font-medium hover:text-[#ff7e22] transition-colors'">En</button>
          </div>

          <button @click="showQuote = true" class="hidden sm:flex items-center gap-2 bg-[#fac130] text-awabot-carbon px-5 py-2.5 rounded-full font-bold text-[14px] hover:bg-awabot-orange hover:text-[#F5F6F7] transition-all group">
            {{ t.nav.quote }}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="bg-[#F5F6F7] rounded-full p-0.5 text-awabot-carbon group-hover:bg-transparent group-hover:text-[#F5F6F7] transition-colors"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <!-- Mobile Menu Button -->
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="lg:hidden p-2 text-awabot-carbon">
            <svg v-if="!mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </button>
        </div>
      </nav>

      <transition 
        enter-active-class="transition duration-300 ease-out"
        enter-from-class="opacity-0 -translate-y-4"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition duration-200 ease-in"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 -translate-y-4"
      >
        <div v-if="mobileMenuOpen" class="lg:hidden bg-awabot-chalk border-t border-awabot-carbon/10 absolute top-20 left-0 right-0 shadow-xl p-8 flex flex-col gap-6 font-switzer">
          <a href="#" class="text-xl font-bold text-awabot-carbon">{{ t.nav.about }}</a>
          <a href="#" class="text-xl font-bold text-awabot-carbon">{{ t.nav.robots }}</a>
          <a href="#" class="text-xl font-bold text-awabot-carbon">{{ t.nav.usage }}</a>
          <a href="#" class="text-xl font-bold text-awabot-carbon">{{ t.nav.news }}</a>
          <div class="h-px bg-awabot-carbon/10 my-2"></div>
          <a href="#" class="flex items-center gap-3 text-lg font-bold text-awabot-carbon/60">{{ t.nav.help }}</a>
          <a href="#" class="flex items-center gap-3 text-lg font-bold text-awabot-carbon/60">{{ t.nav.manage }}</a>
          <button @click="showQuote = true; mobileMenuOpen = false" class="bg-[#fac130] text-awabot-carbon w-full py-4 rounded-full font-bold text-lg mt-4">
            {{ t.nav.quote }}
          </button>
        </div>
      </transition>
    </header>

    <main class="relative pt-32 font-switzer">
      <!-- Hero Section -->
      <div class="max-w-[1700px] ml-auto overflow-hidden">
        <div class="max-w-[1600px] mx-auto px-6 h-full flex flex-col lg:flex-row items-center py-12 lg:py-0">
          <div class="w-full lg:w-[48%] py-12 lg:py-20 relative z-10 hero-content text-center lg:text-left">
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-switzer font-bold text-awabot-carbon leading-[1.1] tracking-tight mb-12">
              <span class="text-awabot-orange font-array font-normal">Awabot</span> <br class="hidden lg:block" />{{ t.hero.title }}
            </h1>
            
            <button
              @click="showQuote = true"
              class="group inline-flex items-center gap-6 bg-[#fac130] hover:bg-[#F9B520] pl-10 pr-3 py-3 rounded-full text-[18px] font-bold text-awabot-carbon transition-all shadow-sm hover:shadow-md active:scale-95"
            >
              {{ t.nav.quote }}
              <div class="w-10 h-10 bg-[#F5F6F7] rounded-full flex items-center justify-center shadow-sm transition-transform group-hover:translate-x-1">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="text-[#fac130]"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </div>
            </button>
          </div>

          <div class="w-full lg:w-[52%] flex justify-end">
            <div class="hero-image relative w-full h-[500px] md:h-[600px] lg:h-[680px] overflow-hidden rounded-l-[180px] md:rounded-l-[280px] lg:rounded-l-[380px] shadow-xl">
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
      <section class="py-32 px-8 overflow-hidden bg-awabot-chalk">
        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row items-center gap-20">
          <div class="w-full lg:w-1/2">
            <p class="text-awabot-orange font-bold uppercase tracking-widest text-sm mb-6">{{ t.features.beam.label }}</p>
            <h2 class="text-4xl md:text-5xl font-array font-normal text-awabot-carbon mb-8 leading-tight">
              {{ t.features.beam.title }}
            </h2>
            <p class="text-[19px] text-awabot-carbon/60 leading-relaxed mb-10 max-w-xl">
              {{ t.features.beam.desc }}
            </p>
            <div class="flex flex-wrap gap-4">
              <button class="bg-[#ff7e22] text-[#F5F6F7] px-8 py-3 rounded-full font-bold hover:opacity-90 transition-all">{{ t.btns.more }}</button>
            </div>
          </div>
          <div class="w-full lg:w-1/2 relative">
            <div class="relative w-full aspect-[4/3] rounded-[60px] overflow-hidden bg-awabot-chalk flex items-center justify-center border border-awabot-carbon/5">
               <!-- Product Image Placeholder -->
               <img src="/hero-robot.png" alt="Beam Robots" class="w-full h-full object-contain p-12" />
            </div>
          </div>
        </div>
      </section>

      <!-- Feature Section 2: Education -->
      <section class="py-32 px-8 bg-awabot-carbon/5">
        <div class="max-w-7xl mx-auto flex flex-col-reverse lg:flex-row items-center gap-20">
          <div class="w-full lg:w-1/2 relative">
            <div class="relative w-full aspect-[4/3] rounded-[60px] overflow-hidden shadow-2xl shadow-awabot-carbon/10">
               <!-- Classroom Image Placeholder -->
               <img src="/telepresence.png" alt="Education" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="w-full lg:w-1/2">
            <p class="text-awabot-orange font-bold uppercase tracking-widest text-sm mb-6">{{ t.features.edu.label }}</p>
            <h2 class="text-4xl md:text-5xl font-array font-normal text-awabot-carbon mb-8 leading-tight">
              {{ t.features.edu.title }}
            </h2>
            <p class="text-[19px] text-awabot-carbon/60 leading-relaxed mb-10">
              {{ t.features.edu.desc }}
            </p>
            <div class="flex flex-wrap gap-4">
              <button class="bg-[#ff7e22] text-[#F5F6F7] px-8 py-3 rounded-full font-bold hover:opacity-90 transition-all">{{ t.btns.more }}</button>
            </div>
          </div>
        </div>
      </section>
      <!-- News Section -->
      <section class="py-24 bg-awabot-chalk overflow-hidden">
        <div class="px-8 md:px-16 mb-16 flex flex-col md:flex-row md:items-end justify-between gap-8">
          <div>
            <p class="text-awabot-orange font-bold text-sm mb-3 uppercase tracking-widest">{{ t.news.label }}</p>
            <h2 class="text-4xl md:text-5xl lg:text-7xl font-array font-normal text-awabot-carbon tracking-tight leading-[0.9]">{{ t.news.title }}</h2>
          </div>
          <button class="flex items-center gap-4 bg-[#fac130] hover:opacity-90 text-[#111111] px-10 py-4 rounded-full font-bold transition-all group shrink-0">
            {{ t.news.allArticles }}
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="transition-transform group-hover:translate-x-1"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>
        </div>

        <!-- Full Width Masonry-ish Grid -->
        <div class="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-4 h-auto md:h-[900px]">
          <!-- Big Item 1: F1 -->
          <div class="md:col-span-2 md:row-span-2 group relative overflow-hidden cursor-pointer border-r border-b border-white lg:border-none">
            <img src="/f1_awabot.jpg" alt="F1 News" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
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

          <!-- Item 2: TED-i -->
          <div class="md:col-span-1 group relative overflow-hidden cursor-pointer border-r border-b border-white lg:border-none">
            <img src="/photo-tedi_awabot.png" alt="TED-i" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
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

          <!-- Item 3: Flexi Beam -->
          <div class="md:col-span-1 group relative overflow-hidden cursor-pointer border-b border-white lg:border-none">
            <img src="https://awabot.com/wp-content/uploads/2024/09/Beam-office_300ppi.webp" alt="Flexi Beam" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
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

          <!-- Item 4: Olympics -->
          <div class="md:col-span-1 group relative overflow-hidden cursor-pointer border-r border-white lg:border-none">
            <img src="https://awabot.com/wp-content/uploads/2024/09/Couverture-article_Awalettre-1-min-1.webp" alt="Olympics" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
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

          <!-- Item 5: HIKIKOMORI -->
          <div class="md:col-span-1 group relative overflow-hidden cursor-pointer lg:border-none">
            <img src="/anne-sophieturion.jpg" alt="HIKU" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
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
      <!-- Trust Section -->
      <section class="py-32 bg-awabot-chalk">
        <div class="max-w-7xl mx-auto px-8 text-center section-header">
          <h2 class="text-4xl font-array font-normal text-awabot-carbon mb-16">
            Ils nous font <span class="text-awabot-orange italic relative shimmer-text inline-block">confiance</span>
          </h2>
          <div class="flex flex-wrap justify-center items-center gap-x-16 gap-y-12 md:gap-x-24 md:gap-y-16 opacity-70 grayscale hover:grayscale-0 transition-all duration-700">
            <img src="https://awabot.com/wp-content/uploads/2024/12/3.png" alt="MESRI" class="h-24 md:h-32 w-auto object-contain" />
            <img src="https://awabot.com/wp-content/uploads/2024/12/2.png" alt="F1" class="h-16 md:h-24 w-auto object-contain" />
            <img src="https://awabot.com/wp-content/uploads/2024/12/1.png" alt="Engie" class="h-14 md:h-20 w-auto object-contain" />
            <img src="https://awabot.com/wp-content/uploads/2024/12/5.png" alt="Paris 2024" class="h-24 md:h-32 w-auto object-contain" />
            <img src="https://awabot.com/wp-content/uploads/2024/12/6.png" alt="EDF" class="h-16 md:h-24 w-auto object-contain" />
          </div>
        </div>
      </section>
    </main>

    <!-- Swiss Style Footer -->
    <footer class="bg-awabot-orange pt-20 pb-12 px-8 md:px-16 text-black font-switzer">
      <div class="max-w-[1700px] mx-auto">
        <div class="mb-24 flex flex-col md:flex-row md:items-end justify-between gap-8">
          <h2 class="text-5xl md:text-7xl lg:text-8xl font-array tracking-tight leading-[0.9]">
            Parlons de vos<br />prochains projets.
          </h2>
        </div>

        <!-- Info Grid -->
        <div class="grid grid-cols-1 md:grid-cols-12 gap-y-12 gap-x-8 mb-20">
          <div class="md:col-span-4">
            <h3 class="text-sm font-bold uppercase tracking-widest mb-6 opacity-40">Contact</h3>
            <div class="flex flex-col text-2xl font-bold leading-[1.1] mb-12">
              <a href="tel:+33437236760" class="hover:opacity-60 transition-opacity">+33 (0)4 37 23 67 60</a>
              <a href="mailto:contact@awabot.com" class="hover:opacity-60 transition-opacity">contact@awabot.com</a>
            </div>
            <a href="/cdc" class="inline-flex items-center gap-3 bg-black text-[#ff7e22] px-6 py-3 rounded-full font-bold text-sm hover:bg-black/80 transition-all">
              Cahier des charges
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="bg-[#ff7e22] rounded-full p-0.5 text-black"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </a>
          </div>
          
          <div class="md:col-span-4">
            <h3 class="text-sm font-bold uppercase tracking-widest mb-6 opacity-40">Adresse</h3>
            <p class="text-2xl font-bold leading-[1.1]">
              16 bis avenue de la République<br />
              69200 Vénissieux, France
            </p>
          </div>

          <div class="md:col-span-4">
            <h3 class="text-sm font-bold uppercase tracking-widest mb-6 opacity-40">Suivez-nous</h3>
            <div class="flex flex-wrap gap-4">
              <a href="#" class="w-12 h-12 rounded-full border-2 border-black/20 flex items-center justify-center hover:bg-black hover:text-awabot-orange transition-all duration-300 group">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"/></svg>
              </a>
              <a href="#" class="w-12 h-12 rounded-full border-2 border-black/20 flex items-center justify-center hover:bg-black hover:text-awabot-orange transition-all duration-300 group">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.25 2.25h6.634l4.717 6.237L18.244 2.25z"/></svg>
              </a>
              <a href="#" class="w-12 h-12 rounded-full border-2 border-black/20 flex items-center justify-center hover:bg-black hover:text-awabot-orange transition-all duration-300 group">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 1.366.062 2.633.332 3.608 1.308.975.975 1.247 2.242 1.308 3.608.058 1.266.07 1.646.07 4.85s-.012 3.584-.07 4.85c-.062 1.366-.332 2.633-1.308 3.608-.975.975-2.242 1.247-3.608 1.308-1.266.058-1.646.07-4.85.07s-3.584-.012-4.85-.07c-1.366-.062-2.633-.332-3.608-1.308-.975-.975-1.247-2.242-1.308-3.608-.058-1.266-.07-1.646-.07-4.85s.012-3.584.07-4.85c.062-1.366.332-2.633 1.308-3.608.975-.975 2.242-1.247 3.608-1.308 1.266-.058 1.646-.07 4.85-.07zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948s.014 3.667.072 4.947c.2 4.337 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072s3.667-.014 4.947-.072c4.336-.2 6.78-2.618 6.98-6.98.058-1.281.072-1.689.072-4.947s-.014-3.667-.072-4.947c-.2-4.349-2.619-6.78-6.98-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.162 6.162 6.162 6.162-2.759 6.162-6.162-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.791-4-4s1.791-4 4-4 4 1.791 4 4-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              </a>
              <a href="#" class="w-12 h-12 rounded-full border-2 border-black/20 flex items-center justify-center hover:bg-black hover:text-awabot-orange transition-all duration-300 group">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.872.505 9.377.505 9.377.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
              </a>
            </div>
          </div>
        </div>

        <!-- Bottom Bar -->
        <div class="pt-8 border-t border-black/10 flex flex-col md:flex-row justify-between items-end gap-8">
          <div class="flex flex-col gap-6">
            <img src="/logo_baseline.svg" alt="Awabot" class="h-8 w-auto brightness-0" />
            <div class="flex gap-6 text-[11px] font-bold uppercase tracking-widest opacity-40">
              <a href="#" class="hover:opacity-100 transition-opacity">Mentions Légales</a>
              <a href="#" class="hover:opacity-100 transition-opacity">Confidentialité</a>
              <a href="#" class="hover:opacity-100 transition-opacity">Cookies</a>
            </div>
          </div>
          <div class="text-[11px] font-bold uppercase tracking-widest opacity-40">
            © {{ new Date().getFullYear() }} Awabot — International Telepresence Experts.
          </div>
        </div>
      </div>
    </footer>

    <!-- Quote Form Overlay -->
    <Transition name="fade">
      <div v-if="showQuote" class="fixed inset-0 z-[100] bg-[#F5F6F7] overflow-y-auto font-switzer">
        <div class="max-w-4xl mx-auto px-8 py-12 md:py-20 relative">
          <!-- Form Header -->
          <div class="flex justify-between items-start mb-12">
            <div>
              <img src="/logo_baseline.svg" alt="Awabot" class="h-10 w-auto mb-8" />
              <p class="text-awabot-carbon/60 text-[18px] leading-tight max-w-2xl">
                {{ t.quoteForm.intro }}
              </p>
            </div>
            <button @click="showQuote = false" class="text-awabot-carbon/40 hover:text-awabot-carbon transition-colors p-2 bg-awabot-carbon/5 rounded-lg">
              <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
          </div>

          <!-- Form Content -->
          <form @submit.prevent class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-10">
            <!-- Vous souhaitez ? -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-awabot-carbon/40 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.wish }} <span class="text-awabot-orange">*</span>
              </label>
              <select class="w-full bg-awabot-carbon/5 border-none rounded-lg px-5 py-4 text-awabot-carbon focus:ring-2 focus:ring-awabot-orange transition-all appearance-none cursor-pointer">
                <option>{{ t.quoteForm.options.wish1 }}</option>
                <option>{{ t.quoteForm.options.wish2 }}</option>
              </select>
            </div>

            <!-- Civilité -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-awabot-carbon/40 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.civility }}
              </label>
              <select class="w-full bg-awabot-carbon/5 border-none rounded-lg px-5 py-4 text-awabot-carbon focus:ring-2 focus:ring-awabot-orange transition-all appearance-none cursor-pointer">
                <option>{{ t.quoteForm.options.madame }}</option>
                <option>{{ t.quoteForm.options.monsieur }}</option>
              </select>
            </div>

            <!-- Identité (Prénom / Nom) -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-awabot-carbon/40 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.identity }} <span class="text-awabot-orange">*</span>
              </label>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <input type="text" class="w-full bg-awabot-carbon/5 border-none rounded-lg px-5 py-4 text-awabot-carbon focus:ring-2 focus:ring-awabot-orange transition-all" />
                  <span class="text-xs text-awabot-carbon/40 mt-1 block">{{ t.quoteForm.fields.firstName }}</span>
                </div>
                <div>
                  <input type="text" class="w-full bg-awabot-carbon/5 border-none rounded-lg px-5 py-4 text-awabot-carbon focus:ring-2 focus:ring-awabot-orange transition-all" />
                  <span class="text-xs text-awabot-carbon/40 mt-1 block">{{ t.quoteForm.fields.lastName }}</span>
                </div>
              </div>
            </div>

            <!-- Société -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-awabot-carbon/40 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.company }}
              </label>
              <input type="text" class="w-full bg-awabot-carbon/5 border-none rounded-lg px-5 py-4 text-awabot-carbon focus:ring-2 focus:ring-awabot-orange transition-all" />
            </div>

            <!-- Secteur -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-awabot-carbon/40 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.sector }}
              </label>
              <select class="w-full bg-awabot-carbon/5 border-none rounded-lg px-5 py-4 text-awabot-carbon focus:ring-2 focus:ring-awabot-orange transition-all appearance-none cursor-pointer">
                <option>{{ t.quoteForm.options.tertiary }}</option>
                <option>{{ t.quoteForm.options.industry }}</option>
                <option>{{ t.quoteForm.options.education }}</option>
                <option>{{ t.quoteForm.options.health }}</option>
              </select>
            </div>

            <!-- Téléphone -->
            <div>
              <label class="block text-[15px] font-bold text-awabot-carbon/40 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.phone }} <span class="text-awabot-orange">*</span>
              </label>
              <input type="tel" class="w-full bg-awabot-carbon/5 border-none rounded-lg px-5 py-4 text-awabot-carbon focus:ring-2 focus:ring-awabot-orange transition-all" />
            </div>

            <!-- Email -->
            <div>
              <label class="block text-[15px] font-bold text-awabot-carbon/40 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.email }} <span class="text-awabot-orange">*</span>
              </label>
              <input type="email" class="w-full bg-awabot-carbon/5 border-none rounded-lg px-5 py-4 text-awabot-carbon focus:ring-2 focus:ring-awabot-orange transition-all" />
            </div>

            <!-- Message -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-awabot-carbon/40 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.message }} <span class="text-awabot-orange">*</span>
              </label>
              <textarea rows="6" class="w-full bg-awabot-carbon/5 border-none rounded-lg px-5 py-4 text-awabot-carbon focus:ring-2 focus:ring-awabot-orange transition-all resize-none"></textarea>
            </div>

            <!-- Terms -->
            <div class="md:col-span-2">
              <p class="text-awabot-carbon/40 text-sm italic leading-tight">
                {{ t.quoteForm.gdpr }}
                <a href="#" class="text-awabot-orange underline">{{ t.quoteForm.privacyLink }}</a>.
              </p>
            </div>

            <!-- Submit -->
            <div class="md:col-span-2 pt-6">
              <button class="bg-[#ff7e22] hover:opacity-90 text-[#F5F6F7] px-12 py-4 rounded-lg font-bold text-lg transition-all active:scale-95 shadow-lg shadow-[#ff7e22]/10">
                {{ t.quoteForm.submit }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const lang = ref('fr')
const showQuote = ref(false)
const mobileMenuOpen = ref(false)

// Watcher to prevent background scroll when quote form is open
watch(showQuote, (val) => {
  if (typeof window !== 'undefined') {
    document.body.style.overflow = val ? 'hidden' : ''
  }
})

onMounted(() => {
  // Loading animations
  const tl = gsap.timeline({ defaults: { ease: 'power3.out', duration: 1 } })
  
  tl.from('.hero-content > *', {
    y: 50,
    opacity: 0,
    stagger: 0.15,
    delay: 0.5
  })
  .from('.hero-image', {
    x: 100,
    opacity: 0,
    duration: 1.2
  }, '-=0.8')
  .from('header', {
    y: -100,
    opacity: 0,
    duration: 0.8
  }, '-=1')

  // Scroll animations
  gsap.utils.toArray('.section-header').forEach((header) => {
    gsap.from(header, {
      scrollTrigger: {
        trigger: header,
        start: 'top 85%',
        toggleActions: 'play none none none'
      },
      y: 40,
      opacity: 0,
      duration: 1,
      ease: 'power2.out'
    })
  })

  // Subtle shimmer effect for "confiance"
  gsap.to('.shimmer-text', {
    backgroundPosition: '200% center',
    duration: 5,
    repeat: -1,
    ease: 'none'
  })
})

const translations = {
  fr: {
    nav: {
      about: 'À propos',
      robots: 'Robots Beam®',
      usage: 'Usages',
      news: 'Actualités',
      help: "Besoin d'aide ?",
      manage: 'Gérer Beam®',
      contactUs: 'Contactez-nous !',
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
    },
    quoteForm: {
      intro: "Utilisez ce formulaire pour entrer en contact avec notre équipe technique, commerciale ou notre service communication. Nous reviendrons vers vous aussi vite que possible.",
      submit: 'Envoyer',
      gdpr: "Awabot collecte vos données afin de répondre à votre demande de contact. Les données marquées d'un astérisque sont obligatoires au traitement de votre demande. Vous pouvez retirer votre consentement à tout moment. Pour plus d'information ou pour exercer vos droits, consultez notre",
      privacyLink: "politique de confidentialité",
      fields: {
        wish: "Vous souhaitez ?",
        civility: "Civilité",
        identity: "Identité",
        firstName: "Prénom",
        lastName: "Nom",
        company: "Société",
        sector: "Secteur",
        phone: "Téléphone",
        email: "Email",
        message: "Décrivez en quelques mots votre besoin ou demande. Vous serez recontacté.e dans les meilleurs délais."
      },
      options: {
        wish1: "Obtenir des informations sur nos dispositifs de téléprésence",
        wish2: "Autre demande",
        madame: "Madame",
        monsieur: "Monsieur",
        tertiary: "Tertiaire",
        industry: "Industrie",
        education: "Éducation",
        health: "Santé"
      }
    }
  },
  en: {
    nav: {
      about: 'About',
      robots: 'Beam® Robots',
      usage: 'Usage',
      news: 'News',
      help: 'Need help?',
      manage: 'Manage Beam®',
      contactUs: 'Contact us!',
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
    },
    quoteForm: {
      intro: "Use this form to get in touch with our technical, sales or communications team. We will get back to you as soon as possible.",
      submit: 'Send',
      gdpr: "Awabot collects your data in order to respond to your contact request. Data marked with an asterisk is required to process your request. You can withdraw your consent at any time. For more information or to exercise your rights, see our",
      privacyLink: "privacy policy",
      fields: {
        wish: "What do you wish?",
        civility: "Civility",
        identity: "Identity",
        firstName: "First Name",
        lastName: "Last Name",
        company: "Company",
        sector: "Sector",
        phone: "Phone",
        email: "Email",
        message: "Describe your needs or request in a few words. You will be contacted as soon as possible."
      },
      options: {
        wish1: "Obtain information about our telepresence devices",
        wish2: "Other request",
        madame: "Ms.",
        monsieur: "Mr.",
        tertiary: "Tertiary",
        industry: "Industry",
        education: "Education",
        health: "Health"
      }
    }
  }
}

const t = computed(() => translations[lang.value])
</script>

<style scoped>
/* Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.transition-all {
  transition: all 0.2s ease-in-out;
}

.shimmer-text {
  background: linear-gradient(
    90deg, 
    #FF7E22 0%, 
    #FF7E22 45%, 
    #FFD1B0 50%, 
    #FF7E22 55%, 
    #FF7E22 100%
  );
  background-size: 200% auto;
  color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
}
</style>

