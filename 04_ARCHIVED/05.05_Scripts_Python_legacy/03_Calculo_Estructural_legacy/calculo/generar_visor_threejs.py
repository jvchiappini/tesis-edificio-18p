"""
====================================================================
 GENERADOR VISOR 3D WEB (THREE.JS) â€” MODELO ESTRUCTURAL EDIFICIO 18P
 Edificio 18P + 3 Subsuelos | MetodologÃ­a BIM ISO 19650
====================================================================

Lee `outputs/elementos_3d.json` (misma fuente de verdad que el IFC) y
genera un visor HTML autocontenido con Three.js (CDN) para visualizar
el modelo estructural 3D sin necesidad de Revit.

  - Losas (transparentes) Â· Pilares Â· Vigas (spandrel / borde pozo)
  - NÃºcleos HÂ°AÂ° N1/N2 Â· Masas de azotea (tanques, piscina)
  - Controles: Ã³rbita/zoom/pan (OrbitControls), corte horizontal por
    nivel, modo wireframe, visibilidad por tipo y etiquetado al clic.

Uso:
  python generar_visor_threejs.py

Salida:
  outputs/visor_3d.html   (abrir en cualquier navegador)

Nota: Three.js se carga desde CDN (jsdelivr). Para uso sin internet,
descargar three.module.js y OrbitControls.js y ajustar las URLs.
====================================================================
"""

import os
import json

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
JSON_PATH = os.path.join(OUT_DIR, "elementos_3d.json")
SALIDA = os.path.join(OUT_DIR, "visor_3d.html")

# â”€â”€ Colores por categorÃ­a (hex) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
C_LOSA = "0x93a6b8"      # gris azulado (transparente)
C_PILAR = "0x3b82f6"     # azul
C_VIGA_SPANDREL = "0x22c55e"   # verde
C_VIGA_BORDE = "0x10b981"      # teal
C_NUCLEO = "0xef4444"     # rojo
C_TANQUE = "0xf59e0b"     # naranja
C_PISCINA = "0x06b6d4"    # cian
C_MASA = "0x8b5cf6"       # violeta (otras masas)


def caja_losa(e):
    z0 = e["z_top"] - e["espesor"]
    return [e["x0"], e["y0"], z0, e["x1"], e["y1"], e["z_top"]]


def caja_pilar(e):
    a = e["ancho"] / 2.0
    return [e["x"] - a, e["y"] - a, e["z0"], e["x"] + a, e["y"] + a, e["z1"]]


def caja_bb(e):
    return [e["x0"], e["y0"], e["z0"], e["x1"], e["y1"], e["z1"]]


def bandas_borde(d):
    """Bandas perimetrales continuas (spandrel 25×50) por nivel, derivadas de
    cada losa. Sustituye en el visor a las 888 cajas segmentadas por tramo
    (el inventario completo por tramo sigue en elementos_3d.json)."""
    bandas = []
    W, H = 0.25, 0.50  # spandrel perimetral (m)
    for L in d["losas"]:
        x0, y0, z_bot, x1, y1, _z_top = caja_losa(L)
        z0, z1 = z_bot - H, z_bot
        for yf in (y0, y1):
            bandas.append([x0, yf - W / 2, z0, x1, yf + W / 2, z1])
        for xf in (x0, x1):
            bandas.append([xf - W / 2, y0, z0, xf + W / 2, y1, z1])
    return [{"b": b, "n": f"banda_{i:03d}", "t": "spandrel"}
            for i, b in enumerate(bandas)]


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as fh:
        d = json.load(fh)

    datos = {
        "niveles": {k: float(v) for k, v in d["cotas"].items()},
        "losas":   [{"b": caja_losa(e), "n": e["id"]} for e in d["losas"]],
        "pilares": [{"b": caja_pilar(e), "n": e["id"]} for e in d["pilares"]],
        "nucleos": [{"b": caja_bb(e), "n": e["id"]} for e in d["nucleos"]],
        "vigas":   bandas_borde(d),
        "vigasB":  [],
        "masas":   [{"b": caja_bb(e), "n": e["id"],
                     "t": e.get("tipo", "masa")} for e in d["masas"]],
    }

    n_total = (len(datos["losas"]) + len(datos["pilares"])
               + len(datos["nucleos"]) + len(datos["vigas"])
               + len(datos["masas"]))
    datos["total"] = n_total

    js_data = json.dumps(datos, ensure_ascii=False)

    html = TEMPLATE.replace("/*__BIM_DATA__*/", js_data)
    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write(html)

    print(f"[OK] {SALIDA}")
    print(f"     {n_total} elementos (losas={len(datos['losas'])}, "
          f"pilares={len(datos['pilares'])}, nucleos={len(datos['nucleos'])}, "
          f"vigas={len(datos['vigas'])}, masas={len(datos['masas'])})")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Visor 3D â€” Modelo Estructural Edificio 18P + 3 Subsuelos</title>
<style>
  :root { --panel: rgba(15,23,42,.88); --txt:#e2e8f0; --acc:#38bdf8; }
  * { box-sizing: border-box; }
  html, body { margin:0; height:100%; overflow:hidden;
    font-family: "Segoe UI", Arial, sans-serif; background:#0b1120; color:var(--txt); }
  #app { position:fixed; inset:0; }
  canvas { display:block; }
  #panel { position:fixed; top:12px; left:12px; width:260px; z-index:10;
    background:var(--panel); border:1px solid rgba(255,255,255,.08);
    border-radius:10px; padding:12px 14px; font-size:13px;
    box-shadow:0 8px 30px rgba(0,0,0,.5); max-height:calc(100vh - 24px);
    overflow:auto; }
  #panel h1 { margin:0 0 2px; font-size:14px; color:#fff; }
  #panel h1 small { display:block; color:#94a3b8; font-weight:400; font-size:11px; }
  #panel .sec { margin-top:10px; border-top:1px solid rgba(255,255,255,.08); padding-top:8px; }
  #panel label { display:flex; align-items:center; gap:7px; padding:2px 0; cursor:pointer; }
  #panel label input { accent-color:var(--acc); }
  .sw { width:11px; height:11px; border-radius:3px; display:inline-block; }
  #panel button { width:100%; margin-top:6px; padding:6px; border:1px solid rgba(255,255,255,.15);
    border-radius:6px; background:rgba(56,189,248,.15); color:#fff; cursor:pointer; font-size:12px; }
  #panel button:hover { background:rgba(56,189,248,.3); }
  #readout { position:fixed; bottom:14px; left:50%; transform:translateX(-50%);
    background:var(--panel); padding:6px 14px; border-radius:8px; font-size:12px;
    border:1px solid rgba(255,255,255,.1); z-index:10; pointer-events:none;
    min-height:20px; text-align:center; }
  #legend { position:fixed; top:12px; right:12px; z-index:10; background:var(--panel);
    border:1px solid rgba(255,255,255,.08); border-radius:8px; padding:10px 12px;
    font-size:12px; display:grid; gap:4px; }
  #legend .it { display:flex; align-items:center; gap:7px; }
  #cutWrap { display:flex; align-items:center; gap:8px; }
  input[type=range] { width:100%; accent-color:var(--acc); }
  .kbd { color:#94a3b8; font-size:11px; }
  #stats { color:#94a3b8; font-size:11px; margin-top:4px; }
</style>
</head>
<body>
<div id="app"></div>

<div id="panel">
  <h1>Modelo Estructural â€” Edificio 18P + 3 Subsuelos
    <small>Three.js Â· datos de modelo_estructural.py Â· ISO 19650</small></h1>
  <div class="sec" id="toggles"></div>
  <div class="sec">
    <div style="margin-bottom:4px"><b>Corte horizontal</b></div>
    <div id="cutWrap">
      <input type="range" id="cut" min="-12" max="68" step="0.5" value="28" disabled>
      <label style="white-space:nowrap"><input type="checkbox" id="cutOn" style="accent-color:var(--acc)"> Activar</label>
    </div>
    <div class="kbd" id="cutVal">Plano de corte: â€”</div>
  </div>
  <div class="sec">
    <button id="wire">Modo wireframe: OFF</button>
    <button id="reset">Restablecer cÃ¡mara</button>
    <button id="explode" style="display:none"></button>
  </div>
  <div class="sec">
    <div><b>Controles</b></div>
    <div class="kbd">Orbit: botÃ³n izq Â· Pan: botÃ³n der Â· Zoom: rueda<br>Clic en un elemento: muestra su etiqueta</div>
  </div>
  <div id="stats"></div>
</div>

<div id="legend"></div>
<div id="readout">Haz clic sobre un elemento para identificarlo</div>

<script type="importmap">
{ "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
} }
</script>
<script type="module">
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const BIM = /*__BIM_DATA__*/;

// â”€â”€ ConfiguraciÃ³n por tipo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
const CFG = [
  { key:'losas',   label:'Losas',             color:'0x93a6b8',        op:0.38 },
  { key:'pilares', label:'Pilares',           color:'0x3b82f6',       op:1.0  },
  { key:'nucleos', label:'NÃºcleos HÂ°AÂ°',      color:'0xef4444',       op:1.0  },
  { key:'vigas',   label:'Vigas (spandrel)',  color:'0x22c55e',       op:1.0 },
  { key:'vigasB',  label:'Vigas (borde pozo)',color:'0x10b981',       op:1.0  },
  { key:'masas',   label:'Masas azotea',      color:'0x8b5cf6',       op:1.0  },
];
const coloresPorTipo = {
  losas:'0x93a6b8', pilares:'0x3b82f6', nucleos:'0xef4444',
  spandrel:'0x22c55e', borde:'0x10b981',
  tanque:'0xf59e0b', piscina:'0x06b6d4', masa:'0x8b5cf6',
};

// â”€â”€ Escena â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
const app = document.getElementById('app');
const renderer = new THREE.WebGLRenderer({ antialias:true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
renderer.shadowMap.enabled = false;
app.appendChild(renderer.domElement);

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0b1120);

const camera = new THREE.PerspectiveCamera(50, innerWidth/innerHeight, 0.5, 2000);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.08;
controls.target.set(45, 28, 21.5);
controls.maxPolarAngle = Math.PI * 0.92;

// Luces
scene.add(new THREE.AmbientLight(0xffffff, 0.55));
const dir = new THREE.DirectionalLight(0xffffff, 1.1);
dir.position.set(120, 180, 90);
scene.add(dir);
const hem = new THREE.HemisphereLight(0x8ec5ff, 0x223, 0.6);
scene.add(hem);

// Rejilla y ejes
const grid = new THREE.GridHelper(120, 24, 0x334155, 0x1e293b);
grid.position.y = -10.5;
scene.add(grid);
const axes = new THREE.AxesHelper(12);
axes.position.set(0, -10.5, 0);
scene.add(axes);

// â”€â”€ ConstrucciÃ³n de mallas â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
const grupos = {
  losas: new THREE.Group(), pilares: new THREE.Group(),
  nucleos: new THREE.Group(), vigas: new THREE.Group(), masas: new THREE.Group(),
};
const geoCache = new Map();
function addBox(grp, [x0,y0,z0,x1,y1,z1], color, op, id) {
  // Mapeo de coordenadas del modelo -> Three.js:
  //   modelo X (ancho, 2.5..87.5)  -> three.x
  //   modelo Y (profundidad, 3..40) -> three.z
  //   modelo Z (elevación, -10.5..67.3) -> three.y  (eje "arriba")
  const w = x1-x0, h = z1-z0, d = y1-y0;
  const k = w.toFixed(3)+'|'+h.toFixed(3)+'|'+d.toFixed(3);
  let geo = geoCache.get(k);
  if (!geo) { geo = new THREE.BoxGeometry(w, h, d); geoCache.set(k, geo); }
  const mat = new THREE.MeshStandardMaterial({ color, transparent: op<1, opacity: op,
    roughness:0.55, metalness:0.1 });
  const mesh = new THREE.Mesh(geo, mat);
  mesh.position.set((x0+x1)/2, (z0+z1)/2, (y0+y1)/2);
  mesh.userData = { id, _b: [x0,y0,z0,x1,y1,z1] };
  grp.add(mesh);
}

for (const s of BIM.losas) addBox(grupos.losas, s.b, coloresPorTipo.losas, 0.38, s.n);
for (const s of BIM.pilares) addBox(grupos.pilares, s.b, coloresPorTipo.pilares, 1.0, s.n);
for (const s of BIM.nucleos) addBox(grupos.nucleos, s.b, coloresPorTipo.nucleos, 1.0, s.n);
for (const s of BIM.vigas) {
  const col = coloresPorTipo[s.t] || coloresPorTipo.spandrel;
  addBox(grupos.vigas, s.b, col, 1.0, s.n);
  const m = grupos.vigas.children[grupos.vigas.children.length-1];
  m.userData.tipo = s.t || 'spandrel';
}
for (const s of BIM.masas) {
  const col = coloresPorTipo[s.t] || coloresPorTipo.masa;
  addBox(grupos.masas, s.b, col, 1.0, s.n);
}
for (const g of Object.values(grupos)) scene.add(g);

// â”€â”€ Panel de visibilidad â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
const togglesEl = document.getElementById('toggles');
const vis = { losas:true, pilares:true, nucleos:true, vigas:true, vigasB:true, masas:true };
const legendEl = document.getElementById('legend');
for (const c of CFG) {
  const lab = document.createElement('label');
  const chk = document.createElement('input'); chk.type='checkbox'; chk.checked = true;
  chk.addEventListener('change', () => {
    vis[c.key] = chk.checked;
    applyCut();
  });
  lab.appendChild(chk);
  const sw = document.createElement('span');
  sw.className='sw'; sw.style.background = c.color;
  lab.appendChild(sw);
  lab.appendChild(document.createTextNode(c.label));
  togglesEl.appendChild(lab);
  const li = document.createElement('div'); li.className='it';
  const s2 = document.createElement('span'); s2.className='sw'; s2.style.background=c.color;
  li.appendChild(s2); li.appendChild(document.createTextNode(c.label));
  legendEl.appendChild(li);
}

// â”€â”€ Visibilidad por tipo + corte horizontal â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
const cutEl = document.getElementById('cut');
const cutOn = document.getElementById('cutOn');
const cutVal = document.getElementById('cutVal');

function tipoVisible(key, tipo) {
  if (key === 'vigas') return tipo === 'borde' ? vis.vigasB : vis.vigas;
  return vis[key] !== false;
}

function applyVis() {
  for (const [key, grp] of Object.entries(grupos)) {
    grp.visible = vis[key] !== false;
    for (const m of grp.children) {
      m.visible = tipoVisible(key, m.userData.tipo);
    }
  }
}

function applyCut() {
  const on = cutOn.checked;
  if (!on) {
    applyVis();
    cutVal.textContent = 'Plano de corte: â€”';
    return;
  }
  const z = parseFloat(cutEl.value);
  for (const [key, grp] of Object.entries(grupos)) {
    grp.visible = true;
    for (const m of grp.children) {
      const b = m.userData._b;
      m.visible = tipoVisible(key, m.userData.tipo) && (b[2] < z && b[5] > z);
    }
  }
  cutVal.textContent = `Plano de corte: Z = ${z.toFixed(2)} m`;
}
cutEl.addEventListener('input', applyCut);
cutOn.addEventListener('change', () => { cutEl.disabled = !cutOn.checked; applyCut(); });

applyCut();

// â”€â”€ Wireframe â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
let wire = false;
const wireBtn = document.getElementById('wire');
wireBtn.addEventListener('click', () => {
  wire = !wire;
  wireBtn.textContent = 'Modo wireframe: ' + (wire ? 'ON' : 'OFF');
  for (const grp of Object.values(grupos)) {
    for (const m of grp.children) { m.material.wireframe = wire; }
  }
});

// â”€â”€ IdentificaciÃ³n al clic â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
const readout = document.getElementById('readout');
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
renderer.domElement.addEventListener('pointerdown', (ev) => {
  mouse.x = (ev.clientX / innerWidth) * 2 - 1;
  mouse.y = -(ev.clientY / innerHeight) * 2 + 1;
  raycaster.setFromCamera(mouse, camera);
  const all = [];
  for (const grp of Object.values(grupos)) grp.traverse(o => { if (o.isMesh && o.visible) all.push(o); });
  const hits = raycaster.intersectObjects(all, false);
  if (hits.length) {
    readout.textContent = hits[0].object.userData.id;
  }
});

// â”€â”€ CÃ¡mara inicial y redimensionado â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
camera.position.set(150, 120, 150);
controls.update();

addEventListener('resize', () => {
  camera.aspect = innerWidth/innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});

document.getElementById('reset').addEventListener('click', () => {
  camera.position.set(150, 120, 150);
  controls.target.set(45, 28, 21.5);
  controls.update();
});

document.getElementById('stats').textContent =
  `Niveles: ${Object.keys(BIM.niveles).length} Â· Elementos: ${BIM.total}`;

(function animate(){
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()