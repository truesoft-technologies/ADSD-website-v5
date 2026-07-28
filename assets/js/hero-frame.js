/* ==========================================================================
   hero-frame.js
   A procedural steel portal-frame skeleton that erects itself in the
   real sequence a crew would follow: setting-out grid -> columns ->
   rafters -> eave & ridge -> purlins -> bracing.
   Drawn as one buffer geometry, revealed with setDrawRange.
   ========================================================================== */
import * as THREE from 'three';

const canvas = document.getElementById('hero-canvas');
if (canvas) init(canvas);

function init(canvas) {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const w0 = window.innerWidth;

  /* ---- adaptive quality tiers ---- */
  const tier = w0 < 640 ? 'low' : w0 < 1200 ? 'mid' : 'high';
  const CFG = {
    low:  { bays: 4, purlins: 2, dpr: 1.5, grid: 2.5 },
    mid:  { bays: 5, purlins: 3, dpr: 1.75, grid: 2 },
    high: { bays: 7, purlins: 3, dpr: 2, grid: 2 }
  }[tier];

  const INK = 0x0b1014;
  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(INK, 26, 96);

  const camera = new THREE.PerspectiveCamera(38, 1, 0.1, 200);
  camera.position.set(19, 9.6, 29);
  camera.lookAt(0, 4.4, 0);

  const renderer = new THREE.WebGLRenderer({
    canvas, antialias: tier !== 'low', alpha: true, powerPreference: 'high-performance'
  });
  renderer.setClearColor(0x000000, 0);

  /* ---- geometry ------------------------------------------------------- */
  const SPAN = 17, EAVE = 6.1, APEX = 8.9, BAY = 5.2;
  const bays = CFG.bays;
  const zs = Array.from({ length: bays + 1 }, (_, i) => (i - bays / 2) * BAY);

  const pos = [], col = [];
  const C_MAIN = new THREE.Color(0x00a9e8);
  const C_SEC  = new THREE.Color(0x8fb6c9);
  const C_GRID = new THREE.Color(0x3d5f72);
  const C_BRC  = new THREE.Color(0x6cd800);

  const seg = (a, b, c, i = 1) => {
    pos.push(a[0], a[1], a[2], b[0], b[1], b[2]);
    col.push(c.r * i, c.g * i, c.b * i, c.r * i, c.g * i, c.b * i);
  };

  /* 1 — setting-out grid on the slab */
  const gx = SPAN / 2 + 4, gz = (bays * BAY) / 2 + 4;
  for (let x = -gx; x <= gx; x += CFG.grid) seg([x, 0, -gz], [x, 0, gz], C_GRID, 0.55);
  for (let z = -gz; z <= gz; z += CFG.grid) seg([-gx, 0, z], [gx, 0, z], C_GRID, 0.55);

  /* 2 — columns + base plates */
  zs.forEach((z) => {
    [-SPAN / 2, SPAN / 2].forEach((x) => {
      seg([x, 0, z], [x, EAVE, z], C_MAIN);
      const s = 0.52;
      seg([x - s, 0.02, z - s], [x + s, 0.02, z - s], C_SEC, 0.8);
      seg([x + s, 0.02, z - s], [x + s, 0.02, z + s], C_SEC, 0.8);
      seg([x + s, 0.02, z + s], [x - s, 0.02, z + s], C_SEC, 0.8);
      seg([x - s, 0.02, z + s], [x - s, 0.02, z - s], C_SEC, 0.8);
    });
  });

  /* 3 — rafters + haunches */
  zs.forEach((z) => {
    seg([-SPAN / 2, EAVE, z], [0, APEX, z], C_MAIN);
    seg([SPAN / 2, EAVE, z], [0, APEX, z], C_MAIN);
    seg([-SPAN / 2 + 1.5, EAVE + 0.78, z], [-SPAN / 2, EAVE - 1.5, z], C_SEC, 0.9);
    seg([SPAN / 2 - 1.5, EAVE + 0.78, z], [SPAN / 2, EAVE - 1.5, z], C_SEC, 0.9);
  });

  /* 4 — eave beams + ridge */
  for (let i = 0; i < bays; i++) {
    const a = zs[i], b = zs[i + 1];
    seg([-SPAN / 2, EAVE, a], [-SPAN / 2, EAVE, b], C_MAIN, 0.9);
    seg([SPAN / 2, EAVE, a], [SPAN / 2, EAVE, b], C_MAIN, 0.9);
    seg([0, APEX, a], [0, APEX, b], C_MAIN, 0.9);
  }

  /* 5 — purlins along both rafter slopes */
  const lerp = (t, side) => [
    side * (SPAN / 2) * (1 - t),
    EAVE + (APEX - EAVE) * t
  ];
  for (let i = 0; i < bays; i++) {
    const a = zs[i], b = zs[i + 1];
    for (let p = 1; p <= CFG.purlins; p++) {
      const t = p / (CFG.purlins + 1);
      [-1, 1].forEach((side) => {
        const [x, y] = lerp(t, side);
        seg([x, y, a], [x, y, b], C_SEC, 0.62);
      });
    }
  }

  /* 6 — bracing in the end bays (roof plan + side walls) */
  [[zs[0], zs[1]], [zs[bays - 1], zs[bays]]].forEach(([a, b]) => {
    [-1, 1].forEach((side) => {
      const [x1, y1] = lerp(0.06, side), [x2, y2] = lerp(0.9, side);
      seg([x1, y1, a], [x2, y2, b], C_BRC, 0.5);
      seg([x2, y2, a], [x1, y1, b], C_BRC, 0.5);
      seg([side * SPAN / 2, 0.1, a], [side * SPAN / 2, EAVE, b], C_BRC, 0.42);
      seg([side * SPAN / 2, EAVE, a], [side * SPAN / 2, 0.1, b], C_BRC, 0.42);
    });
  });

  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  geo.setAttribute('color', new THREE.Float32BufferAttribute(col, 3));
  const total = pos.length / 3;
  geo.setDrawRange(0, reduce ? total : 0);

  const frame = new THREE.LineSegments(
    geo,
    new THREE.LineBasicMaterial({ vertexColors: true, transparent: true, opacity: 1 })
  );
  const group = new THREE.Group();
  group.add(frame);
  group.rotation.y = -0.32;
  scene.add(group);

  /* faint depth haze plane behind the frame */
  const haze = new THREE.Mesh(
    new THREE.PlaneGeometry(120, 60),
    new THREE.MeshBasicMaterial({ color: 0x0d3d55, transparent: true, opacity: 0.16 })
  );
  haze.position.set(0, 8, -46);
  scene.add(haze);

  /* ---- sizing --------------------------------------------------------- */
  function resize() {
    const r = canvas.getBoundingClientRect();
    const w = r.width || window.innerWidth, h = r.height || window.innerHeight;
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, CFG.dpr));
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    /* pull the camera back on narrow viewports so the frame still reads */
    const k = w / h;
    camera.position.set(19, 9.6, k < 1 ? 46 : k < 1.4 ? 37 : 29);
    camera.lookAt(0, 4.4, 0);
    camera.updateProjectionMatrix();
  }
  resize();
  let rt;
  window.addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(resize, 140); }, { passive: true });

  /* ---- erection sequence ---------------------------------------------- */
  const state = { drawn: reduce ? total : 0 };
  window.ADSD_ERECT = () => {
    if (reduce) return;
    if (window.gsap) {
      window.gsap.to(state, {
        drawn: total, duration: 3.4, ease: 'power2.inOut',
        onUpdate: () => geo.setDrawRange(0, Math.floor(state.drawn))
      });
    } else {
      geo.setDrawRange(0, total);
    }
  };

  /* the loader may have finished before this module evaluated */
  if (window.__adsdErect) window.ADSD_ERECT();

  /* ---- interaction ---------------------------------------------------- */
  const ptr = { x: 0, y: 0, tx: 0, ty: 0 };
  if (!reduce && window.matchMedia('(hover: hover)').matches) {
    window.addEventListener('pointermove', (e) => {
      ptr.tx = (e.clientX / window.innerWidth - 0.5) * 2;
      ptr.ty = (e.clientY / window.innerHeight - 0.5) * 2;
    }, { passive: true });
  }

  /* ---- render loop, gated on visibility ------------------------------- */
  let visible = true, running = false, raf = 0;
  new IntersectionObserver(([e]) => {
    visible = e.isIntersecting;
    visible ? start() : stop();
  }, { threshold: 0.02 }).observe(canvas);
  document.addEventListener('visibilitychange', () => {
    document.hidden ? stop() : (visible && start());
  });

  const clock = new THREE.Clock();
  function tick() {
    if (!running) return;
    raf = requestAnimationFrame(tick);
    const t = clock.getElapsedTime();
    ptr.x += (ptr.tx - ptr.x) * 0.045;
    ptr.y += (ptr.ty - ptr.y) * 0.045;
    group.rotation.y = -0.32 + Math.sin(t * 0.055) * 0.09 + ptr.x * 0.1;
    group.rotation.x = ptr.y * 0.035;
    group.position.y = Math.sin(t * 0.32) * 0.16;
    camera.position.y = 9.6 - ptr.y * 0.9;
    camera.lookAt(0, 4.4, 0);
    renderer.render(scene, camera);
  }
  function start() { if (!running) { running = true; clock.getDelta(); tick(); } }
  function stop() { running = false; cancelAnimationFrame(raf); }

  renderer.render(scene, camera);
  canvas.classList.add('on');
  start();
}
