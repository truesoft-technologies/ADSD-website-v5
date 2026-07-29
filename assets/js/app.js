/* ==========================================================================
   app.js — ADSD Steel Technical Services Contracting L.L.C
   Lenis smooth scroll · GSAP + ScrollTrigger · SplitType · Motion One
   Every effect is gated behind prefers-reduced-motion and pointer checks.
   ========================================================================== */
(() => {
  'use strict';

  const REDUCE = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const FINE   = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const $  = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const has = (n) => typeof window[n] !== 'undefined';

  /* ---------------------------------------------------------------- scroll */
  let lenis = null;

  function initScroll() {
    if (REDUCE || !has('Lenis')) { document.documentElement.style.scrollBehavior = 'smooth'; return; }
    lenis = new Lenis({
      duration: 1.05,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
      touchMultiplier: 1.6
    });
    if (has('gsap') && has('ScrollTrigger')) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((t) => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    } else {
      const raf = (t) => { lenis.raf(t); requestAnimationFrame(raf); };
      requestAnimationFrame(raf);
    }
  }

  const scrollTo = (target) => {
    const el = typeof target === 'string' ? $(target) : target;
    if (!el) return;
    if (lenis) lenis.scrollTo(el, { offset: -70, duration: 1.15 });
    else el.scrollIntoView({ behavior: REDUCE ? 'auto' : 'smooth' });
  };

  /* ---------------------------------------------------------------- loader */
  function initLoader(onDone) {
    const box = $('.loader');
    if (!box || REDUCE || !has('gsap')) {
      if (box) box.remove();
      document.body.classList.add('is-ready');
      onDone();
      return;
    }
    document.body.classList.add('is-locked');
    if (lenis) lenis.stop();

    const num = $('.loader__n', box);
    const counter = { v: 0 };

    gsap.timeline({
      onComplete: () => {
        box.remove();
        document.body.classList.remove('is-locked');
        if (lenis) lenis.start();
        document.body.classList.add('is-ready');
        onDone();
      }
    })
      .to('.loader__logo', { opacity: 1, duration: .6, ease: 'power2.out' })
      .to('.loader__fill', { scaleX: 1, duration: 1.15, ease: 'power2.inOut' }, .15)
      .to(counter, {
        v: 100, duration: 1.15, ease: 'power2.inOut',
        onUpdate: () => { if (num) num.textContent = String(Math.round(counter.v)).padStart(3, '0'); }
      }, .15)
      .to('.loader__inner', { opacity: 0, y: -14, duration: .45, ease: 'power2.in' }, '+=.12')
      .to('.loader__curtain', { scaleY: 0, duration: .85, ease: 'expo.inOut' }, '-=.15');
  }

  /* ------------------------------------------------------------------- nav */
  function initNav() {
    const nav = $('.nav');
    const burger = $('.burger');
    const menu = $('.menu');
    if (!nav) return;

    let last = 0;
    const onScroll = () => {
      const y = window.scrollY;
      nav.classList.toggle('nav--solid', y > window.innerHeight * 0.86);
      nav.classList.toggle('nav--hidden', y > last && y > 480 && !document.body.classList.contains('menu-open'));
      last = y;
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    if (burger && menu) {
      const toggle = (open) => {
        document.body.classList.toggle('menu-open', open);
        burger.setAttribute('aria-expanded', String(open));
        menu.setAttribute('aria-hidden', String(!open));
        if (lenis) open ? lenis.stop() : lenis.start();
      };
      burger.addEventListener('click', () => toggle(!document.body.classList.contains('menu-open')));
      $$('a', menu).forEach((a) => a.addEventListener('click', () => toggle(false)));
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && document.body.classList.contains('menu-open')) toggle(false);
      });
    }

    /* in-page anchors */
    $$('a[href^="#"]').forEach((a) => {
      const id = a.getAttribute('href');
      if (!id || id === '#' || !$(id)) return;
      a.addEventListener('click', (e) => { e.preventDefault(); scrollTo(id); });
    });

    /* section spy */
    const ids = $$('[data-nav-link]')
      .map((a) => a.getAttribute('href'))
      .filter((h) => h && h.charAt(0) === '#' && h.length > 1 && $(h));
    if (ids.length) {
      const io = new IntersectionObserver((es) => {
        es.forEach((en) => {
          if (!en.isIntersecting) return;
          $$('[data-nav-link]').forEach((a) => {
            a.toggleAttribute('aria-current', a.getAttribute('href') === '#' + en.target.id);
            if (a.getAttribute('href') === '#' + en.target.id) a.setAttribute('aria-current', 'page');
          });
        });
      }, { rootMargin: '-45% 0px -50% 0px' });
      ids.forEach((h) => io.observe($(h)));
    }
  }

  /* --------------------------------------------------------------- reveals */
  function initReveals() {
    if (!has('gsap') || !has('ScrollTrigger')) {
      $$('[data-reveal],[data-reveal-x],[data-img-reveal]').forEach((el) => {
        el.style.opacity = 1; el.style.transform = 'none'; el.style.clipPath = 'none';
      });
      return;
    }
    if (REDUCE) return;

    $$('[data-reveal]').forEach((el) => {
      gsap.to(el, {
        opacity: 1, y: 0, duration: .95, ease: 'power3.out',
        delay: parseFloat(el.dataset.delay || 0),
        scrollTrigger: { trigger: el, start: 'top 88%', once: true }
      });
    });

    /* staggered groups */
    $$('[data-stagger]').forEach((grp) => {
      const kids = Array.from(grp.children);
      gsap.set(kids, { opacity: 0, y: 26 });
      // Cap the total spread so large grids (e.g. the all-products grid)
      // don't take many seconds for the last items to fade in.
      const each = Math.min(.085, 3.5 / kids.length);
      gsap.to(kids, {
        opacity: 1, y: 0, duration: .85, ease: 'power3.out', stagger: each,
        scrollTrigger: { trigger: grp, start: 'top 84%', once: true }
      });
    });

    /* image clip reveals */
    $$('[data-img-reveal]').forEach((el) => {
      gsap.to(el, {
        clipPath: 'inset(0 0 0% 0)', duration: 1.25, ease: 'expo.out',
        scrollTrigger: { trigger: el, start: 'top 90%', once: true }
      });
    });

    /* parallax */
    $$('[data-parallax]').forEach((el) => {
      gsap.to(el, {
        yPercent: parseFloat(el.dataset.parallax) || -12, ease: 'none',
        scrollTrigger: { trigger: el.closest('.media,.phero__bg,.cta__bg') || el, start: 'top bottom', end: 'bottom top', scrub: true }
      });
    });

    /* split-text line reveals */
    if (has('SplitType')) {
      $$('[data-split]').forEach((el) => {
        const s = new SplitType(el, { types: 'lines,words', lineClass: 'st-line' });
        $$('.st-line', el).forEach((l) => { l.style.overflow = 'hidden'; });
        gsap.from(s.words, {
          yPercent: 108, duration: 1, ease: 'expo.out', stagger: .018,
          scrollTrigger: { trigger: el, start: 'top 86%', once: true }
        });
      });
    }

    /* process bars */
    $$('.proc__bar').forEach((b) => {
      gsap.to(b, {
        scaleX: 1, duration: 1.1, ease: 'expo.out',
        scrollTrigger: { trigger: b.parentElement, start: 'top 85%', once: true }
      });
    });

    /* table rows */
    $$('[data-rows] tbody tr').forEach((tr, i) => {
      gsap.from(tr, {
        opacity: 0, y: 14, duration: .6, ease: 'power2.out', delay: i * .045,
        scrollTrigger: { trigger: tr.closest('[data-rows]'), start: 'top 82%', once: true }
      });
    });
  }

  /* -------------------------------------------------------------- hero text */
  function heroIn() {
    const h1 = $('[data-hero-h]');
    if (!has('gsap')) return;
    const tl = gsap.timeline({ defaults: { ease: 'expo.out' } });

    if (h1 && has('SplitType') && !REDUCE) {
      const s = new SplitType(h1, { types: 'lines,words', lineClass: 'st-line' });
      $$('.st-line', h1).forEach((l) => { l.style.overflow = 'hidden'; });
      gsap.set(h1, { opacity: 1 });
      tl.from(s.words, { yPercent: 112, duration: 1.15, stagger: .035 }, 0);
    } else if (h1) {
      tl.from(h1, { opacity: 0, y: 24, duration: .9 }, 0);
    }

    tl.from('[data-hero-eye]', { opacity: 0, y: 14, duration: .7 }, .1)
      .from('[data-hero-sub]', { opacity: 0, y: 18, duration: .85 }, .35)
      .from('[data-hero-act] > *', { opacity: 0, y: 16, duration: .7, stagger: .09 }, .5)
      .from('[data-hero-spec] > *', { opacity: 0, y: 20, duration: .8, stagger: .07 }, .62);

    if (typeof window.ADSD_ERECT === 'function') window.ADSD_ERECT();
    window.__adsdErect = true;
  }

  /* -------------------------------------------------------------- counters */
  function initCounters() {
    $$('[data-count]').forEach((el) => {
      const to = parseFloat(el.dataset.count);
      const dec = (el.dataset.dec | 0);
      const pre = el.dataset.pre || '', suf = el.dataset.suf || '';
      const write = (v) => { el.textContent = pre + v.toFixed(dec) + suf; };
      if (REDUCE || !has('gsap')) { write(to); return; }
      write(0);
      const o = { v: 0 };
      gsap.to(o, {
        v: to, duration: 1.9, ease: 'power2.out',
        onUpdate: () => write(o.v),
        scrollTrigger: { trigger: el, start: 'top 92%', once: true }
      });
    });
  }

  /* --------------------------------------------------------------- marquee */
  function initMarquee() {
    $$('.marq').forEach((m) => {
      const track = $('.marq__track', m);
      const grp = $('.marq__grp', track);
      if (!track || !grp) return;
      /* duplicate until the track comfortably overflows twice */
      while (track.scrollWidth < m.offsetWidth * 2.2 && track.children.length < 12) {
        const c = grp.cloneNode(true);
        c.setAttribute('aria-hidden', 'true');
        track.appendChild(c);
      }
      if (REDUCE || !has('gsap')) return;
      const w = grp.getBoundingClientRect().width;
      gsap.to(track, { x: -w, duration: w / 42, ease: 'none', repeat: -1 });
    });
  }

  /* ------------------------------------------------------- magnetic buttons */
  function initMagnetic() {
    if (!FINE || REDUCE) return;
    const spring = has('Motion') && Motion.animate;
    $$('[data-magnet]').forEach((el) => {
      const strength = parseFloat(el.dataset.magnet) || 0.24;
      const move = (e) => {
        const r = el.getBoundingClientRect();
        const x = (e.clientX - (r.left + r.width / 2)) * strength;
        const y = (e.clientY - (r.top + r.height / 2)) * strength;
        if (spring) Motion.animate(el, { x, y }, { type: 'spring', stiffness: 320, damping: 22 });
        else if (has('gsap')) gsap.to(el, { x, y, duration: .4, ease: 'power3.out' });
      };
      const out = () => {
        if (spring) Motion.animate(el, { x: 0, y: 0 }, { type: 'spring', stiffness: 260, damping: 18 });
        else if (has('gsap')) gsap.to(el, { x: 0, y: 0, duration: .55, ease: 'elastic.out(1,.4)' });
      };
      el.addEventListener('pointermove', move);
      el.addEventListener('pointerleave', out);
    });
  }

  /* --------------------------------------------- service hover preview card */
  function initPeek() {
    const peek = $('.peek');
    if (!peek || !FINE || REDUCE || !has('gsap')) return;
    const img = $('img', peek);
    const rows = $$('[data-peek]');
    if (!rows.length) return;
    const qx = gsap.quickTo(peek, 'x', { duration: .55, ease: 'power3' });
    const qy = gsap.quickTo(peek, 'y', { duration: .55, ease: 'power3' });
    let on = false;
    let scrolling = false;
    let scrollTimer;

    const hide = () => {
      if (!on) return;
      on = false;
      gsap.to(peek, { opacity: 0, scale: .92, duration: .3, ease: 'power2.in' });
    };

    /* Chromium (and others) synthesise pointerenter/pointerleave from a
       hit-test change even when the pointer itself never moved — which is
       exactly what happens as these stacked rows scroll past a stationary
       cursor. That can re-show the peek mid-scroll, or land on a state with
       no matching "leave" at all, leaving the thumbnail stuck on screen.
       Rather than race that, hover is ignored entirely while scrolling is
       in progress, and forced hidden for the duration. */
    const onScroll = () => {
      scrolling = true;
      hide();
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(() => { scrolling = false; }, 140);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    if (lenis) lenis.on('scroll', onScroll);

    rows.forEach((row) => {
      row.addEventListener('pointerenter', () => {
        if (scrolling) return;
        img.src = row.dataset.peek;
        img.alt = '';
        on = true;
        gsap.to(peek, { opacity: 1, scale: 1, duration: .45, ease: 'power3.out' });
      });
      row.addEventListener('pointerleave', hide);
    });
    window.addEventListener('pointermove', (e) => {
      if (!on) return;
      qx(e.clientX - 130); qy(e.clientY - 220);
    }, { passive: true });
  }

  /* ------------------------------------------------------------- accordion */
  function initFaq() {
    $$('.faq__i').forEach((item) => {
      const btn = $('.faq__q', item), panel = $('.faq__a', item);
      if (!btn || !panel) return;
      btn.addEventListener('click', () => {
        const open = item.classList.contains('on');
        const sibs = $$('.faq__i', item.parentElement);
        sibs.forEach((s) => {
          if (s === item) return;
          s.classList.remove('on');
          $('.faq__q', s).setAttribute('aria-expanded', 'false');
          const p = $('.faq__a', s);
          if (has('gsap')) gsap.to(p, { height: 0, duration: .4, ease: 'power2.inOut' });
          else p.style.height = '0px';
        });
        item.classList.toggle('on', !open);
        btn.setAttribute('aria-expanded', String(!open));
        if (has('gsap')) {
          gsap.to(panel, { height: open ? 0 : 'auto', duration: .5, ease: 'power2.inOut' });
        } else {
          panel.style.height = open ? '0px' : 'auto';
        }
      });
    });
  }

  /* -------------------------------------------------------------- lightbox */
  function initLightbox() {
    const box = $('.lbox');
    if (!box) return;
    const img = $('.lbox img', box), cap = $('.lbox__cap', box);
    const items = $$('.gal__i');
    if (!items.length) return;
    let i = 0;

    const show = (n) => {
      i = (n + items.length) % items.length;
      const src = items[i].dataset.full || $('img', items[i]).src;
      img.src = src;
      img.alt = $('img', items[i]).alt || '';
      cap.textContent = ($('img', items[i]).alt || '') + '  ·  ' + (i + 1) + ' / ' + items.length;
    };
    const open = (n) => {
      show(n); box.classList.add('on'); box.setAttribute('aria-hidden', 'false');
      if (lenis) lenis.stop(); document.body.classList.add('is-locked');
      $('.lbox__x', box).focus();
    };
    const close = () => {
      box.classList.remove('on'); box.setAttribute('aria-hidden', 'true');
      if (lenis) lenis.start(); document.body.classList.remove('is-locked');
    };

    items.forEach((el, n) => {
      el.setAttribute('role', 'button');
      el.setAttribute('tabindex', '0');
      el.addEventListener('click', () => open(n));
      el.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(n); } });
    });
    $('.lbox__x', box).addEventListener('click', close);
    $('.lbox__nav--p', box).addEventListener('click', () => show(i - 1));
    $('.lbox__nav--n', box).addEventListener('click', () => show(i + 1));
    box.addEventListener('click', (e) => { if (e.target === box) close(); });
    document.addEventListener('keydown', (e) => {
      if (!box.classList.contains('on')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(i - 1);
      if (e.key === 'ArrowRight') show(i + 1);
    });
  }

  /* ------------------------------------------------------------------ form */
  function initForm() {
    const form = $('[data-form]');
    if (!form) return;
    const ok = $('.form__ok', form);

    const bad = (f, msg) => {
      f.classList.add('bad');
      const e = $('.f__err', f);
      if (e) e.textContent = msg;
    };

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let valid = true;
      $$('.f', form).forEach((f) => f.classList.remove('bad'));

      $$('[required]', form).forEach((el) => {
        const f = el.closest('.f');
        if (!f) return;
        if (!el.value.trim()) { bad(f, 'Required'); valid = false; return; }
        if (el.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(el.value)) {
          bad(f, 'Enter a valid email address'); valid = false;
        }
      });
      if (!valid) { $('.f.bad input, .f.bad select, .f.bad textarea', form)?.focus(); return; }

      /* No backend is wired up. Hand the enquiry to the user's mail client
         so the form is genuinely usable on a static host. */
      const g = (n) => (form.elements[n]?.value || '').trim();
      const body = [
        'Name: ' + g('name'),
        'Company: ' + g('company'),
        'Email: ' + g('email'),
        'Phone: ' + g('phone'),
        'Scope: ' + g('scope'),
        '',
        g('message')
      ].join('\n');
      const to = form.dataset.mailto || 'ads.techdxb@gmail.com';
      window.location.href = 'mailto:' + to
        + '?subject=' + encodeURIComponent('Enquiry — ' + (g('scope') || 'General') + ' — ' + g('company'))
        + '&body=' + encodeURIComponent(body);

      if (ok) {
        ok.classList.add('on');
        ok.setAttribute('role', 'status');
      }
      form.reset();
    });
  }

  /* ------------------------------------------------------------ table rows */
  function initTableLinks() {
    $$('[data-rows] tbody tr[data-href]').forEach((tr) => {
      tr.tabIndex = 0;
      const go = (e) => {
        const href = tr.dataset.href;
        if (e.metaKey || e.ctrlKey || e.button === 1) { window.open(href, '_blank'); return; }
        window.location.href = href;
      };
      tr.addEventListener('click', (e) => {
        if (e.target.closest('a')) return;
        go(e);
      });
      tr.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(e); }
      });
    });
  }

  /* ------------------------------------------------------------------ boot */
  function boot() {
    initScroll();
    initNav();
    initMarquee();
    initMagnetic();
    initPeek();
    initFaq();
    initLightbox();
    initForm();
    initTableLinks();
    initReveals();
    initCounters();
    if (has('ScrollTrigger')) ScrollTrigger.refresh();
    initLoader(heroIn);
    window.addEventListener('load', () => { if (has('ScrollTrigger')) ScrollTrigger.refresh(); });
  }

  if (has('gsap') && has('ScrollTrigger')) gsap.registerPlugin(ScrollTrigger);
  document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', boot)
    : boot();
})();
