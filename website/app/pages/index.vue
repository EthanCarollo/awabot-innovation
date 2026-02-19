<template>
  <div class="min-h-screen bg-white selection:bg-awabot-orange/20">
    <!-- Header -->
    <header class="relative z-50 flex items-center justify-between px-8 md:px-16 py-8">
      <nav class="hidden md:flex items-center gap-10">
        <NuxtLink to="/" class="text-[16px] font-bold text-slate-900 hover:text-awabot-orange transition-colors">
          {{ t.nav.about }}
        </NuxtLink>
        <NuxtLink to="/" class="text-[16px] font-bold text-slate-900 hover:text-awabot-orange transition-colors">
          {{ t.nav.robots }}
        </NuxtLink>
        <NuxtLink to="/" class="text-[16px] font-bold text-slate-900 hover:text-awabot-orange transition-colors">
          {{ t.nav.usage }}
        </NuxtLink>
        <NuxtLink to="/" class="text-[16px] font-bold text-slate-900 hover:text-awabot-orange transition-colors">
          {{ t.nav.news }}
        </NuxtLink>
      </nav>

      <div class="md:absolute md:left-1/2 md:-translate-x-1/2">
        <img src="/logo_baseline.svg" alt="Awabot" class="h-10 w-auto" />
      </div>

      <nav class="hidden md:flex items-center gap-8">
        <NuxtLink to="/" class="flex items-center gap-2 text-[15px] font-bold text-slate-900 hover:text-awabot-orange transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          {{ t.nav.help }}
        </NuxtLink>
        <NuxtLink to="/" class="flex items-center gap-2 text-[15px] font-bold text-slate-900 hover:text-awabot-orange transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          {{ t.nav.manage }}
        </NuxtLink>
        <button 
          @click="showQuote = true"
          class="flex items-center gap-2 text-[15px] font-bold text-slate-900 hover:text-awabot-orange transition-colors"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path><polyline points="10 17 15 12 10 7"></polyline><line x1="15" y1="12" x2="3" y2="12"></line></svg>
          {{ t.nav.contactUs }}
        </button>
        <div class="flex items-center gap-1.5 text-[15px] font-bold ml-4">
          <button 
            @click="lang = 'fr'" 
            :class="lang === 'fr' ? 'text-awabot-orange border-b-2 border-awabot-orange' : 'text-slate-800 opacity-60 hover:opacity-100'"
            class="transition-all"
          >FR</button>
          <span class="text-slate-300">|</span>
          <button 
            @click="lang = 'en'" 
            :class="lang === 'en' ? 'text-awabot-orange border-b-2 border-awabot-orange' : 'text-slate-800 opacity-60 hover:opacity-100'"
            class="transition-all"
          >EN</button>
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
            <h1 class="text-[44px] md:text-[58px] lg:text-[76px] leading-[1.05] tracking-tight text-slate-900 mb-14">
              <span class="text-awabot-orange font-array">Awabot</span> 
              <span class="font-switzer font-semibold">{{ t.hero.title }}</span>
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
            <img src="https://awabot.com/wp-content/uploads/2024/12/Couverture-article_F1-Lyon-Robot.webp" alt="F1 News" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
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
        <div class="max-w-7xl mx-auto px-8 text-center">
          <h2 class="text-4xl font-array font-normal text-slate-900 mb-16">
            Ils nous font <span class="text-awabot-orange italic">confiance</span>
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
            <div class="flex gap-4">
              <a href="#" class="w-10 h-10 rounded-full border border-black/10 flex items-center justify-center hover:border-slate-800 hover:text-awabot-orange transition-all"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path></svg></a>
              <a href="#" class="w-10 h-10 rounded-full border border-black/10 flex items-center justify-center hover:border-slate-800 hover:text-awabot-orange transition-all"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
              <a href="#" class="w-10 h-10 rounded-full border border-black/10 flex items-center justify-center hover:border-slate-800 hover:text-awabot-orange transition-all"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
              <a href="#" class="w-10 h-10 rounded-full border border-black/10 flex items-center justify-center hover:border-slate-800 hover:text-awabot-orange transition-all"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg></a>
              <a href="#" class="w-10 h-10 rounded-full border border-black/10 flex items-center justify-center hover:border-slate-800 hover:text-awabot-orange transition-all"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
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
import { ref, computed } from 'vue'

const lang = ref('fr')
const showQuote = ref(false)

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
</style>

