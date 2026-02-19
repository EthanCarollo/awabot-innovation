<template>
  <div class="min-h-screen bg-white selection:bg-awabot-orange/20">
    <!-- Navigation -->
    <header class="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-100 h-24">
      <nav class="max-w-[1700px] mx-auto px-8 h-full flex items-center justify-between relative">
        <!-- Left: Desktop Nav Links -->
        <div class="hidden lg:flex items-center gap-6">
          <a href="#" class="text-[15px] font-bold text-slate-900 transition-colors hover:text-awabot-orange whitespace-nowrap">{{ t.nav.about }}</a>
          <a href="#" class="text-[15px] font-bold text-slate-900 transition-colors hover:text-awabot-orange whitespace-nowrap">{{ t.nav.robots }}</a>
          <a href="#" class="text-[15px] font-bold text-slate-900 transition-colors hover:text-awabot-orange whitespace-nowrap">{{ t.nav.usage }}</a>
          <a href="#" class="text-[15px] font-bold text-slate-900 transition-colors hover:text-awabot-orange whitespace-nowrap">{{ t.nav.news }}</a>
        </div>

        <!-- Center: Logo -->
        <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
          <a href="/" class="flex flex-col items-center pointer-events-auto cursor-pointer">
            <span class="font-array text-awabot-orange text-3xl leading-none">awabot</span>
            <span class="text-[9px] uppercase tracking-[0.2em] font-bold text-slate-400 -mt-0.5">Closer than ever.</span>
          </a>
        </div>

        <!-- Right: Actions -->
        <div class="flex items-center gap-4">
          <!-- Desktop Secondary Nav -->
          <div class="hidden 2xl:flex items-center gap-6 border-r border-slate-100 pr-6 mr-2">
            <a href="#" class="flex items-center gap-2 text-[13px] font-bold text-slate-600 hover:text-slate-900 transition-colors whitespace-nowrap">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 1 1-7.6-12.7 8.35 8.35 0 0 1 4.3 1.25L21 3v8.5z"></path></svg>
              {{ t.nav.help }}
            </a>
            <a href="#" class="flex items-center gap-2 text-[13px] font-bold text-slate-600 hover:text-slate-900 transition-colors whitespace-nowrap">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
              {{ t.nav.manage }}
            </a>
          </div>

          <div class="flex items-center gap-2 text-[14px] font-extrabold mr-4 min-w-[60px] justify-center">
            <button @click="lang = 'fr'" :class="lang === 'fr' ? 'text-awabot-orange border-b-2 border-awabot-orange' : 'text-slate-400'">FR</button>
            <span class="text-slate-200">|</span>
            <button @click="lang = 'en'" :class="lang === 'en' ? 'text-awabot-orange border-b-2 border-awabot-orange' : 'text-slate-400'">EN</button>
          </div>

          <button @click="showQuote = true" class="hidden sm:flex items-center gap-3 bg-awabot-yellow text-slate-900 px-6 py-3 rounded-full font-bold text-[14px] hover:bg-awabot-orange hover:text-white transition-all group">
            {{ t.nav.quote }}
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="bg-white rounded-full p-0.5 text-slate-900 group-hover:bg-transparent group-hover:text-white transition-colors"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <!-- Mobile Menu Button -->
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="lg:hidden p-2 text-slate-900">
            <svg v-if="!mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </button>
        </div>
      </nav>

      <!-- Mobile Menu Overlay -->
      <transition 
        enter-active-class="transition duration-300 ease-out"
        enter-from-class="opacity-0 -translate-y-4"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition duration-200 ease-in"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 -translate-y-4"
      >
        <div v-if="mobileMenuOpen" class="lg:hidden bg-white border-t border-slate-100 absolute top-24 left-0 right-0 shadow-xl p-8 flex flex-col gap-6">
          <a href="#" class="text-xl font-bold text-slate-900">{{ t.nav.about }}</a>
          <a href="#" class="text-xl font-bold text-slate-900">{{ t.nav.robots }}</a>
          <a href="#" class="text-xl font-bold text-slate-900">{{ t.nav.usage }}</a>
          <a href="#" class="text-xl font-bold text-slate-900">{{ t.nav.news }}</a>
          <div class="h-px bg-slate-100 my-2"></div>
          <a href="#" class="flex items-center gap-3 text-lg font-bold text-slate-600">{{ t.nav.help }}</a>
          <a href="#" class="flex items-center gap-3 text-lg font-bold text-slate-600">{{ t.nav.manage }}</a>
          <button @click="showQuote = true; mobileMenuOpen = false" class="bg-awabot-yellow text-slate-900 w-full py-4 rounded-full font-bold text-lg mt-4">
            {{ t.nav.quote }}
          </button>
        </div>
      </transition>
    </header>

    <main class="relative pt-24">
      <!-- Hero Section -->
      <div class="max-w-[1700px] ml-auto overflow-hidden">
        <div class="max-w-[1600px] mx-auto px-6 h-full flex flex-col lg:flex-row items-center py-12 lg:py-0">
          <div class="w-full lg:w-[48%] py-12 lg:py-20 relative z-10 hero-content text-center lg:text-left">
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-switzer font-bold text-slate-900 leading-[1.1] tracking-tight mb-12">
              <span class="text-awabot-orange font-array font-normal">Awabot</span> <br class="hidden lg:block" />{{ t.hero.title }}
            </h1>
            
            <button
              @click="showQuote = true"
              class="group inline-flex items-center gap-6 bg-awabot-yellow hover:bg-[#F9B520] pl-10 pr-3 py-3 rounded-full text-[18px] font-bold text-slate-900 transition-all shadow-sm hover:shadow-md active:scale-95"
            >
              {{ t.nav.quote }}
              <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-sm transition-transform group-hover:translate-x-1">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="text-awabot-yellow"><polyline points="9 18 15 12 9 6"></polyline></svg>
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
      <section class="py-32 px-8 overflow-hidden">
        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row items-center gap-20">
          <div class="w-full lg:w-1/2">
            <p class="text-awabot-orange font-bold uppercase tracking-widest text-sm mb-6">{{ t.features.beam.label }}</p>
            <h2 class="text-4xl md:text-5xl font-array font-normal text-slate-900 mb-8 leading-tight">
              {{ t.features.beam.title }}
            </h2>
            <p class="text-[19px] text-slate-600 leading-relaxed mb-10 max-w-xl">
              {{ t.features.beam.desc }}
            </p>
            <div class="flex flex-wrap gap-4">
              <button class="bg-slate-800 text-white px-8 py-3 rounded-full font-bold hover:bg-slate-700 transition-all">{{ t.btns.more }}</button>
              <button @click="showQuote = true" class="border-2 border-slate-800 text-slate-800 px-8 py-3 rounded-full font-bold hover:bg-slate-50 transition-all">{{ t.btns.contact }}</button>
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
            <h2 class="text-4xl md:text-5xl font-array font-normal text-slate-900 mb-8 leading-tight">
              {{ t.features.edu.title }}
            </h2>
            <p class="text-[19px] text-slate-600 leading-relaxed mb-10">
              {{ t.features.edu.desc }}
            </p>
            <div class="flex flex-wrap gap-4">
              <button class="bg-awabot-orange text-white px-8 py-3 rounded-full font-bold hover:bg-[#FF8B3D] transition-all hover-lift">{{ t.btns.more }}</button>
              <button @click="showQuote = true" class="bg-white border-2 border-awabot-orange text-awabot-orange px-8 py-3 rounded-full font-bold hover:bg-orange-50 transition-all">{{ t.btns.contact }}</button>
            </div>
          </div>
        </div>
      </section>
      <!-- News Section: Full Width & Overlay Style -->
      <section class="py-24 bg-white overflow-hidden">
        <div class="px-8 md:px-16 mb-16 flex flex-col md:flex-row md:items-end justify-between gap-8">
          <div>
            <p class="text-awabot-orange font-bold text-sm mb-3 uppercase tracking-widest">{{ t.news.label }}</p>
            <h2 class="text-4xl md:text-5xl lg:text-7xl font-array font-normal text-slate-900 tracking-tight">{{ t.news.title }}</h2>
          </div>
          <button class="flex items-center gap-4 bg-awabot-yellow hover:bg-[#F9B520] text-slate-900 px-10 py-4 rounded-full font-bold transition-all group shrink-0 hover-lift">
            {{ t.news.allArticles }}
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="transition-transform group-hover:translate-x-1"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>
        </div>

        <!-- Full Width Masonry-ish Grid -->
        <div class="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-4 h-auto md:h-[900px]">
          <!-- Big Item 1: F1 -->
          <div class="md:col-span-2 md:row-span-2 group relative overflow-hidden cursor-pointer border-r border-b border-white lg:border-none">
            <img src="https://awabot.com/wp-content/uploads/2024/12/Couverture-article_F1-Abu-Dhabi.webp" alt="F1 News" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
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
            <img src="https://awabot.com/wp-content/uploads/2024/11/Couverture-TED-i-min.webp" alt="TED-i" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
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
            <img src="https://awabot.com/wp-content/uploads/2024/10/Couverture-article_HIKIKOMORI_Awabot.webp" alt="HIKU" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
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
      <section class="py-32 bg-white">
        <div class="max-w-7xl mx-auto px-8 text-center section-header">
          <h2 class="text-4xl font-array font-normal text-slate-900 mb-16">
            Ils nous font <span class="text-awabot-orange italic relative shimmer-text inline-block">confiance</span>
          </h2>
          <div class="flex flex-wrap justify-center items-center gap-12 md:gap-20 opacity-60 grayscale hover:grayscale-0 transition-all duration-700">
            <img src="https://awabot.com/wp-content/uploads/2024/12/3.png" alt="MESRI" class="h-16 md:h-20 w-auto object-contain" />
            <img src="https://awabot.com/wp-content/uploads/2024/12/2.png" alt="F1" class="h-12 md:h-16 w-auto object-contain" />
            <img src="https://awabot.com/wp-content/uploads/2024/12/1.png" alt="Engie" class="h-10 md:h-14 w-auto object-contain" />
            <img src="https://awabot.com/wp-content/uploads/2024/12/5.png" alt="Paris 2024" class="h-16 md:h-20 w-auto object-contain" />
            <img src="https://awabot.com/wp-content/uploads/2024/12/6.png" alt="EDF" class="h-12 md:h-16 w-auto object-contain" />
          </div>
        </div>
      </section>
    </main>

    <!-- Redesigned Footer -->
    <footer class="bg-awabot-orange py-28 px-8 md:px-16 overflow-hidden relative">
      <div class="max-w-7xl mx-auto">
        <div class="mb-20">
          <p class="text-sm font-bold uppercase tracking-widest text-slate-900 mb-6">Nous contacter</p>
          <div class="flex flex-col lg:flex-row justify-between items-start gap-12">
            <h2 class="text-4xl md:text-5xl lg:text-6xl font-array text-slate-900 leading-[1.1] max-w-4xl">
              Vous souhaitez en savoir plus ?<br />
              <span class="opacity-60">Nous restons à votre écoute !</span>
            </h2>
            <button 
              @click="showQuote = true"
              class="bg-[#E32342] hover:bg-[#C11B35] text-white px-8 py-4 rounded-lg font-bold flex items-center gap-4 transition-all hover-lift shrink-0"
            >
              Nous contacter par email ?
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
          </div>
        </div>
          
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-16 mb-24">
          <div>
            <p class="text-[17px] font-bold text-slate-900 mb-4 font-switzer">Nous écrire :</p>
            <p class="text-xl md:text-2xl font-bold text-slate-900 leading-tight opacity-80">
              16 bis avenue de la République<br />
              69200 Vénissieux
            </p>
          </div>
          <div>
            <p class="text-[17px] font-bold text-slate-900 mb-4 font-switzer">Nous appeler :</p>
            <p class="text-xl md:text-2xl font-bold text-slate-900 opacity-80">
              +33 (0)4 37 23 67 60
            </p>
          </div>
          <div class="flex flex-col gap-6">
            <div class="flex flex-wrap gap-x-8 gap-y-4">
              <a href="#" class="text-sm font-bold uppercase tracking-widest text-slate-900/60 hover:text-slate-900 transition-colors">Twitter</a>
              <a href="#" class="text-sm font-bold uppercase tracking-widest text-slate-900/60 hover:text-slate-900 transition-colors">Facebook</a>
              <a href="#" class="text-sm font-bold uppercase tracking-widest text-slate-900/60 hover:text-slate-900 transition-colors">LinkedIn</a>
              <a href="#" class="text-sm font-bold uppercase tracking-widest text-slate-900/60 hover:text-slate-900 transition-colors">YouTube</a>
              <a href="#" class="text-sm font-bold uppercase tracking-widest text-slate-900/60 hover:text-slate-900 transition-colors">Instagram</a>
            </div>
          </div>
        </div>

        <div class="pt-12 border-t border-black/10 flex flex-col md:flex-row justify-between items-center gap-8 text-center md:text-left">
          <div class="flex flex-col md:flex-row items-center gap-8">
            <div class="flex flex-col gap-1 items-center md:items-start opacity-30">
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-900">Propulsé par :</p>
              <img src="/logo_baseline.svg" alt="Awabot" class="h-8 w-auto brightness-0" />
            </div>
            <div class="flex gap-6 text-[13px] font-bold text-slate-900/40 uppercase tracking-widest">
              <a href="#" class="hover:text-slate-900 transition-colors">Mentions Légales</a>
              <span class="opacity-20">|</span>
              <a href="#" class="hover:text-slate-900 transition-colors">Politique de confidentialité</a>
            </div>
          </div>
          <p class="text-slate-900/30 text-[13px] font-bold uppercase tracking-widest">© {{ new Date().getFullYear() }} Awabot — Tous droits réservés</p>
        </div>
      </div>
    </footer>

    <!-- Quote Form Overlay -->
    <Transition name="fade">
      <div v-if="showQuote" class="fixed inset-0 z-[100] bg-white overflow-y-auto font-switzer">
        <div class="max-w-4xl mx-auto px-8 py-12 md:py-20 relative">
          <!-- Form Header -->
          <div class="flex justify-between items-start mb-12">
            <div>
              <img src="/logo_baseline.svg" alt="Awabot" class="h-10 w-auto mb-8" />
              <p class="text-slate-600 text-[18px] leading-relaxed max-w-2xl">
                {{ t.quoteForm.intro }}
              </p>
            </div>
            <button @click="showQuote = false" class="text-slate-400 hover:text-slate-900 transition-colors p-2 bg-slate-50 rounded-lg">
              <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
          </div>

          <!-- Form Content -->
          <form @submit.prevent class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-10">
            <!-- Vous souhaitez ? -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-slate-500 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.wish }} <span class="text-red-500">*</span>
              </label>
              <select class="w-full bg-slate-50 border-none rounded-lg px-5 py-4 text-slate-800 focus:ring-2 focus:ring-awabot-orange transition-all appearance-none cursor-pointer">
                <option>{{ t.quoteForm.options.wish1 }}</option>
                <option>{{ t.quoteForm.options.wish2 }}</option>
              </select>
            </div>

            <!-- Civilité -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-slate-500 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.civility }}
              </label>
              <select class="w-full bg-slate-50 border-none rounded-lg px-5 py-4 text-slate-800 focus:ring-2 focus:ring-awabot-orange transition-all appearance-none cursor-pointer">
                <option>{{ t.quoteForm.options.madame }}</option>
                <option>{{ t.quoteForm.options.monsieur }}</option>
              </select>
            </div>

            <!-- Identité (Prénom / Nom) -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-slate-500 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.identity }} <span class="text-red-500">*</span>
              </label>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <input type="text" class="w-full bg-slate-50 border-none rounded-lg px-5 py-4 text-slate-800 focus:ring-2 focus:ring-awabot-orange transition-all" />
                  <span class="text-xs text-slate-400 mt-1 block">{{ t.quoteForm.fields.firstName }}</span>
                </div>
                <div>
                  <input type="text" class="w-full bg-slate-50 border-none rounded-lg px-5 py-4 text-slate-800 focus:ring-2 focus:ring-awabot-orange transition-all" />
                  <span class="text-xs text-slate-400 mt-1 block">{{ t.quoteForm.fields.lastName }}</span>
                </div>
              </div>
            </div>

            <!-- Société -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-slate-500 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.company }}
              </label>
              <input type="text" class="w-full bg-slate-50 border-none rounded-lg px-5 py-4 text-slate-800 focus:ring-2 focus:ring-awabot-orange transition-all" />
            </div>

            <!-- Secteur -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-slate-500 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.sector }}
              </label>
              <select class="w-full bg-slate-50 border-none rounded-lg px-5 py-4 text-slate-800 focus:ring-2 focus:ring-awabot-orange transition-all appearance-none cursor-pointer">
                <option>{{ t.quoteForm.options.tertiary }}</option>
                <option>{{ t.quoteForm.options.industry }}</option>
                <option>{{ t.quoteForm.options.education }}</option>
                <option>{{ t.quoteForm.options.health }}</option>
              </select>
            </div>

            <!-- Téléphone -->
            <div>
              <label class="block text-[15px] font-bold text-slate-500 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.phone }} <span class="text-red-500">*</span>
              </label>
              <input type="tel" class="w-full bg-slate-50 border-none rounded-lg px-5 py-4 text-slate-800 focus:ring-2 focus:ring-awabot-orange transition-all" />
            </div>

            <!-- Email -->
            <div>
              <label class="block text-[15px] font-bold text-slate-500 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.email }} <span class="text-red-500">*</span>
              </label>
              <input type="email" class="w-full bg-slate-50 border-none rounded-lg px-5 py-4 text-slate-800 focus:ring-2 focus:ring-awabot-orange transition-all" />
            </div>

            <!-- Message -->
            <div class="md:col-span-2">
              <label class="block text-[15px] font-bold text-slate-500 mb-3 uppercase tracking-wide">
                {{ t.quoteForm.fields.message }} <span class="text-red-500">*</span>
              </label>
              <textarea rows="6" class="w-full bg-slate-50 border-none rounded-lg px-5 py-4 text-slate-800 focus:ring-2 focus:ring-awabot-orange transition-all resize-none"></textarea>
            </div>

            <!-- Terms -->
            <div class="md:col-span-2">
              <p class="text-slate-400 text-sm italic leading-relaxed">
                {{ t.quoteForm.gdpr }}
                <a href="#" class="text-awabot-orange underline">{{ t.quoteForm.privacyLink }}</a>.
              </p>
            </div>

            <!-- Submit -->
            <div class="md:col-span-2 pt-6">
              <button class="bg-[#E32342] hover:bg-[#C11B35] text-white px-12 py-4 rounded-lg font-bold text-lg transition-all hover-lift active:scale-95 shadow-lg shadow-red-500/10">
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

