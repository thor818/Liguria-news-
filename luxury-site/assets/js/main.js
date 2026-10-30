/* Riviera Rent — site logic: contacts, homes, gallery, forms, illustrations. */
(function () {
  "use strict";
  var C = window.FRR_CONFIG || {};
  var HOMES = window.FRR_PROPERTIES || [];
  var LANG = document.documentElement.lang === "fr" ? "fr" : "en";
  var T = {
    en: {
      guests: "guests", studio: "Studio", bed: "bedroom", beds: "bedrooms", bath: "bathroom", baths: "bathrooms",
      pool: "Pool", sea: "Sea view", parking: "Parking", longTerm: "6+ months", from: "from", night: "/ night",
      book: "Book", ask: "Enquire", photos: "photos", close: "Close", empty: "No home matches this filter yet. Call us: we always have something to suggest.",
      copied: "Copied!", copy: "Copy", needMsg: "Please write your name and a message.",
      hello: "Hello Riviera Rent,", about: "I'm interested in", prev: "Previous photo", next: "Next photo",
      offer: "Special offer", guestsShort: "guests", seeHome: "See & book", until: "until"
    },
    fr: {
      guests: "pers.", studio: "Studio", bed: "chambre", beds: "chambres", bath: "salle de bains", baths: "salles de bains",
      pool: "Piscine", sea: "Vue mer", parking: "Parking", longTerm: "6 mois et +", from: "dès", night: "/ nuit",
      book: "Réserver", ask: "Demander", photos: "photos", close: "Fermer", empty: "Aucun logement pour ce filtre pour l'instant. Appelez-nous : nous avons toujours une idée.",
      copied: "Copié !", copy: "Copier", needMsg: "Merci d'indiquer votre nom et un message.",
      hello: "Bonjour Riviera Rent,", about: "Je suis intéressé(e) par", prev: "Photo précédente", next: "Photo suivante",
      offer: "Offre spéciale", guestsShort: "pers.", seeHome: "Voir & réserver", until: "jusqu'au"
    }
  }[LANG];
  var ct = C.contacts || {};
  var ROOT = typeof window.FRR_ROOT === "string" ? window.FRR_ROOT : "/"; // site root (changed only for previews)
  var engine = (C.booking && C.booking.engineUrl && C.booking.engineUrl[LANG]) || "#";
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function wa(text) { return "https://wa.me/" + ct.whatsapp + (text ? "?text=" + encodeURIComponent(text) : ""); }

  /* ---------- Contacts and links from config ---------- */
  function fillContacts() {
    var map = {
      booking: engine, phone: ct.phoneHref, mobile: ct.mobileHref, whatsapp: wa(""),
      email: "mailto:" + ct.email, maps: ct.mapsUrl
    };
    $$("[data-c]").forEach(function (n) {
      var k = n.getAttribute("data-c");
      if (map[k] && n.tagName === "A") n.href = map[k];
      if (k === "phone-text") n.textContent = ct.phone;
      if (k === "mobile-text") n.textContent = ct.mobile;
      if (k === "email-text") n.textContent = ct.email;
      if (k === "address") n.textContent = ct.address;
      if (k === "hours") n.textContent = (ct.hours || {})[LANG] || "";
      if (k === "count") n.textContent = (C.stats && C.stats.homesFR) || HOMES.length;
      if (k === "count-it") n.textContent = (C.stats && C.stats.homesIT) || "65";
    });
    var v = C.booking && C.booking.voucher;
    $$(".voucher").forEach(function (box) {
      if (!v) { box.hidden = true; return; }
      $("code", box).textContent = v;
      $("button", box).addEventListener("click", function (e) {
        e.preventDefault(); e.stopPropagation();
        var b = this;
        (navigator.clipboard ? navigator.clipboard.writeText(v) : Promise.reject()).then(function () {
          b.textContent = T.copied; setTimeout(function () { b.textContent = T.copy; }, 1800);
        }, function () {});
      });
    });
    var y = $(".year"); if (y) y.textContent = new Date().getFullYear();
  }

  /* ---------- Homes ---------- */
  function photo(h, i) { return ROOT + "assets/img/homes/" + h.id + "/" + (i < 9 ? "0" : "") + (i + 1) + ".jpg"; }
  function card(h) {
    var f = [];
    f.push(h.guests + " " + T.guests);
    f.push(h.bedrooms === 0 ? T.studio : h.bedrooms + " " + (h.bedrooms > 1 ? T.beds : T.bed));
    if (h.pool) f.push(T.pool);
    if (h.seaView) f.push(T.sea);
    if (h.parking) f.push(T.parking);
    var facts = f.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + (h.longTerm ? '<li class="lt">' + T.longTerm + "</li>" : "");
    var price = h.fromPrice ? '<span class="price">' + T.from + " <b>€" + esc(h.fromPrice) + "</b> " + T.night + "</span>" : "<span></span>";
    var bookBtn = h.shortTerm
      ? '<a class="btn btn-azur btn-sm" target="_blank" rel="noopener" href="' + esc(h.bookingUrl || engine) + '">' + T.book + "</a>"
      : "";
    return '<article class="card reveal" data-id="' + h.id + '">' +
      '<button class="card-photo" type="button" data-gallery="' + h.id + '" aria-label="' + esc(h.name) + " – " + h.photos + " " + T.photos + '">' +
      '<img loading="lazy" src="' + ROOT + 'assets/img/homes/' + h.id + '/cover.jpg" alt="">' +
      '<span class="card-tag">' + esc((h.tag || {})[LANG] || "") + "</span>" +
      '<span class="card-count">▦ ' + h.photos + "</span></button>" +
      '<div class="card-body"><p class="card-town">' + esc(h.town) + "</p><h3>" + esc(h.name) + "</h3>" +
      "<p>" + esc((h.desc || {})[LANG] || "") + "</p><ul class=\"facts\">" + facts + "</ul>" +
      '<div class="card-foot">' + price + '<div class="card-actions">' + bookBtn +
      '<a class="btn btn-line btn-sm" href="#contact" data-home="' + esc(h.name) + '">' + T.ask + "</a></div></div></div></article>";
  }
  function renderGrid(filter) {
    var grid = $("#grid"); if (!grid) return;
    var list = HOMES.filter(function (h) {
      if (!filter || filter === "all") return true;
      if (filter === "pool") return h.pool;
      if (filter === "long") return h.longTerm;
      return h.area === filter;
    });
    grid.innerHTML = list.map(card).join("");
    $("#grid-empty").hidden = list.length > 0;
    $("#grid-empty").textContent = T.empty;
    observe($$(".reveal", grid));
  }
  function initFilters() {
    $$(".filter").forEach(function (b) {
      b.addEventListener("click", function () {
        $$(".filter").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        renderGrid(b.getAttribute("data-filter"));
      });
    });
    $$("[data-filter-link]").forEach(function (a) {
      a.addEventListener("click", function () {
        var f = $('.filter[data-filter="' + a.getAttribute("data-filter-link") + '"]'); if (f) f.click();
      });
    });
  }


  /* ---------- Offers ---------- */
  function today() { return new Date().toISOString().slice(0, 10); }
  function isLive(o) { var d = today(); return !o.draft && (!o.start || o.start <= d) && (!o.end || o.end >= d); }
  function fmtDate(iso) {
    try { return new Date(iso + "T12:00:00").toLocaleDateString(LANG === "fr" ? "fr-FR" : "en-GB", { day: "numeric", month: "long" }); } catch (e) { return iso; }
  }
  // Offers of the French homes (config.js → offers). The section hides itself when none is live.
  function renderOffers() {
    var box = $("#offers-grid"); if (!box) return;
    var list = (C.offers || []).filter(isLive);
    $("#offers").hidden = !list.length;
    $$('a[href="#offers"]').forEach(function (a) { a.hidden = !list.length; });
    box.innerHTML = list.map(function (o) {
      var h = HOMES.filter(function (x) { return x.id === o.property; })[0] || {};
      var t = o[LANG] || o.en || {};
      return '<article class="offer reveal"><span class="offer-photo"><img loading="lazy" src="' + ROOT + 'assets/img/homes/' + esc(h.id) + '/cover.jpg" alt=""><span class="card-tag">' + esc(o.badge || T.offer) + "</span></span>" +
        '<div class="offer-body"><p class="card-town">' + esc(h.name || "") + " · " + esc(h.town || "") + "</p><h3>" + esc(t.title || "") + "</h3><p>" + esc(t.text || "") + "</p>" +
        '<div class="card-foot"><span class="price">' + T.from + " <b>€" + esc(o.price) + "</b> " + esc(t.unit || "") + (o.end ? "<br><small>" + T.until + " " + fmtDate(o.end) + "</small>" : "") + "</span>" +
        '<a class="btn btn-azur btn-sm" target="_blank" rel="noopener" href="' + esc(h.bookingUrl || engine) + '">' + T.book + "</a></div></div></article>";
    }).join("");
    observe($$(".reveal", box));
  }

  /* ---------- Sister company: homes and offers read live from rivierarent.it ---------- */
  function loadScript(src) {
    return new Promise(function (ok, ko) { var s = document.createElement("script"); s.src = src; s.async = true; s.onload = ok; s.onerror = ko; document.head.appendChild(s); });
  }
  function renderItaly() {
    var box = $("#italy-grid"), S = C.sister; if (!box || !S) return;
    var base = S.dataBase;
    Promise.all([loadScript(base + "/assets/js/properties.js"), loadScript(base + "/assets/js/config.js")]).then(function () {
      var all = window.RR_PROPERTIES || [], cfg = window.RR_CONFIG || {};
      var byId = {}; all.forEach(function (p) { byId[p.id] = p; });
      var live = {}; (cfg.offers || []).filter(isLive).forEach(function (o) { if (byId[o.property] && !live[o.property]) live[o.property] = o; });
      var ids = Object.keys(live).concat((S.featured || []).filter(function (id) { return !live[id]; }));
      var list = ids.map(function (id) { return byId[id]; }).filter(function (p) { return p && p.image; }).slice(0, S.max || 6);
      if (!list.length) throw new Error("no homes");
      box.innerHTML = list.map(function (p) {
        var o = live[p.id], ot = o && (o[LANG] || o.en);
        var img = /^https?:/.test(p.image) ? p.image : base + p.image;
        var price = o && ot ? T.from + " <b>€" + esc(o.price) + "</b> " + esc(ot.unit || "") : p.fromPrice ? T.from + " <b>€" + esc(p.fromPrice) + "</b> " + T.night : "";
        var facts = [p.guests ? p.guests + " " + T.guestsShort : "", p.pool ? T.pool : "", p.seaView ? T.sea : ""].filter(Boolean)
          .map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("");
        return '<a class="it-card" target="_blank" rel="noopener" href="' + esc(p.bookingUrl || S.url[LANG]) + '">' +
          '<span class="it-photo"><img loading="lazy" src="' + esc(img) + '" alt="">' + (o ? '<span class="card-tag tag-offer">' + esc((ot && ot.title) || T.offer) + "</span>" : "") + "</span>" +
          '<span class="it-body"><span class="card-town">Liguria · Italia</span><b>' + esc(p.name) + "</b>" +
          ((p.desc || {})[LANG] ? "<small>" + esc(p.desc[LANG]) + "</small>" : "") + '<ul class="facts">' + facts + "</ul>" +
          '<span class="it-foot"><span class="price">' + price + '</span><span class="it-go">' + T.seeHome + " →</span></span></span></a>";
      }).join("");
      $("#italy").hidden = false;
    }).catch(function () { var s = $("#italy"); if (s) s.hidden = true; });
  }

  /* ---------- Gallery ---------- */
  var lb, cur, idx = 0;
  function openGallery(id) {
    cur = HOMES.filter(function (h) { return h.id === id; })[0]; if (!cur) return;
    idx = 0;
    if (!lb) {
      lb = document.createElement("div");
      lb.className = "lightbox"; lb.setAttribute("role", "dialog"); lb.setAttribute("aria-modal", "true");
      lb.innerHTML = '<div class="lb-top"><p class="lb-title"></p><button class="lb-btn lb-close" aria-label="' + T.close + '">✕</button></div>' +
        '<div class="lb-stage"><button class="lb-btn lb-prev" aria-label="' + T.prev + '">←</button><img alt=""><button class="lb-btn lb-next" aria-label="' + T.next + '">→</button></div>' +
        '<div class="lb-bottom"><span class="lb-count"></span><a class="btn btn-mimosa lb-book" target="_blank" rel="noopener" href="#">' + T.book + ' <i aria-hidden="true">→</i></a></div>';
      document.body.appendChild(lb);
      $(".lb-close", lb).onclick = closeGallery;
      $(".lb-prev", lb).onclick = function () { show(idx - 1); };
      $(".lb-next", lb).onclick = function () { show(idx + 1); };
      var x0 = null;
      $(".lb-stage", lb).addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
      $(".lb-stage", lb).addEventListener("touchend", function (e) {
        if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
        if (Math.abs(dx) > 40) show(idx + (dx < 0 ? 1 : -1));
      });
      document.addEventListener("keydown", function (e) {
        if (!lb || lb.hidden) return;
        if (e.key === "Escape") closeGallery();
        if (e.key === "ArrowRight") show(idx + 1);
        if (e.key === "ArrowLeft") show(idx - 1);
      });
    }
    $(".lb-title", lb).innerHTML = esc(cur.name) + "<small>" + esc(cur.town) + "</small>";
    var book = $(".lb-book", lb);
    if (cur.shortTerm) { book.hidden = false; book.href = cur.bookingUrl || engine; }
    else { book.hidden = false; book.href = "#contact"; book.removeAttribute("target"); book.onclick = closeGallery; }
    lb.hidden = false; document.body.style.overflow = "hidden";
    show(0);
    $(".lb-close", lb).focus();
  }
  function show(i) {
    idx = (i + cur.photos) % cur.photos;
    $(".lb-stage img", lb).src = photo(cur, idx);
    $(".lb-stage img", lb).alt = cur.name + " " + (idx + 1);
    $(".lb-count", lb).textContent = (idx + 1) + " / " + cur.photos;
    new Image().src = photo(cur, (idx + 1) % cur.photos);
  }
  function closeGallery() { if (lb) { lb.hidden = true; document.body.style.overflow = ""; } }

  /* ---------- Contact form: opens WhatsApp or email, nothing stored ---------- */
  function initForm() {
    var form = $("#contact-form"); if (!form) return;
    var how = "whatsapp";
    $$("button[type=submit]", form).forEach(function (b) { b.addEventListener("click", function () { how = b.value; }); });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      if (!String(d.get("name") || "").trim() || !String(d.get("message") || "").trim()) { $("#form-msg").textContent = T.needMsg; return; }
      $("#form-msg").textContent = "";
      var topic = form.topic.options[form.topic.selectedIndex].text;
      var lines = [T.hello, "", T.about + ": " + topic];
      if (d.get("dates")) lines.push(form.dates.getAttribute("data-label") + ": " + d.get("dates"));
      lines.push("", d.get("message"), "", "— " + d.get("name"));
      var text = lines.join("\n");
      if (how === "email") location.href = "mailto:" + ct.email + "?subject=" + encodeURIComponent(topic + " – " + d.get("name")) + "&body=" + encodeURIComponent(text);
      else window.open(wa(text), "_blank", "noopener");
    });
    // Buttons that preselect the topic or mention a home
    document.addEventListener("click", function (e) {
      var a = e.target.closest("[data-topic],[data-home],[data-gallery]");
      if (!a) return;
      if (a.hasAttribute("data-gallery")) { openGallery(a.getAttribute("data-gallery")); return; }
      if (a.hasAttribute("data-topic")) form.topic.value = a.getAttribute("data-topic");
      if (a.hasAttribute("data-home")) {
        var h = HOMES.filter(function (x) { return x.name === a.getAttribute("data-home"); })[0];
        form.topic.value = h && !h.shortTerm ? "long" : "short";
        form.dates.value = a.getAttribute("data-home");
      }
    });
  }

  /* ---------- Header, menu, progress, reveal ---------- */
  function initChrome() {
    var header = $(".site-header"), bar = $(".progress");
    if (!header) return;
    function onScroll() {
      var y = window.scrollY, h = document.documentElement.scrollHeight - innerHeight;
      header.classList.toggle("scrolled", y > 30);
      if (bar) bar.style.transform = "scaleX(" + (h > 0 ? y / h : 0) + ")";
    }
    addEventListener("scroll", onScroll, { passive: true }); onScroll();
    var t = $(".nav-toggle"), nav = $("#nav");
    if (!t || !nav) return;
    t.addEventListener("click", function () {
      var o = t.getAttribute("aria-expanded") !== "true";
      t.setAttribute("aria-expanded", o); nav.classList.toggle("open", o);
      document.body.style.overflow = o ? "hidden" : "";
    });
    $$("a", nav).forEach(function (a) { a.addEventListener("click", function () {
      t.setAttribute("aria-expanded", "false"); nav.classList.remove("open"); document.body.style.overflow = "";
    }); });
  }
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -8% 0px" }) : null;
  function observe(nodes) { nodes.forEach(function (n) { if (io) io.observe(n); else n.classList.add("in"); }); }

  /* ---------- Illustrations ---------- */
  var NS = "http://www.w3.org/2000/svg";
  function el(tag, attrs, parent) {
    var n = document.createElementNS(NS, tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  var seed = 11;
  function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
  function palm(svg, x, base, h, flip) {
    var g = el("g", { class: "palm" }, svg);
    var s = flip ? -1 : 1;
    el("path", { d: "M" + x + " " + base + " Q" + (x + 14 * s) + " " + (base - h / 2) + " " + (x + 6 * s) + " " + (base - h), stroke: "#7a5a3c", "stroke-width": 7, fill: "none", "stroke-linecap": "round" }, g);
    var tx = x + 6 * s, ty = base - h;
    [[-60, 8], [-30, 2], [0, -4], [30, 2], [60, 8], [-85, 18], [85, 18]].forEach(function (a) {
      var ang = a[0] * Math.PI / 180, len = 52;
      var ex = tx + Math.sin(ang) * len, ey = ty - Math.cos(ang) * len * .55 + a[1] + 18;
      el("path", { d: "M" + tx + " " + ty + " Q" + (tx + Math.sin(ang) * len * .55) + " " + (ty - 22) + " " + ex + " " + ey, stroke: "#3f7a58", "stroke-width": 9, fill: "none", "stroke-linecap": "round" }, g);
    });
  }
  // Belle Époque façades of Beausoleil: cream, rose and ochre, wrought-iron balconies, zinc mansards
  function drawFacades() {
    var svg = $("#town"); if (!svg) return;
    var colors = ["#f3e6cf", "#e8b9a8", "#f2d39a", "#efd9c9", "#dfa392", "#f6eedf", "#e9c58a"];
    el("circle", { cx: 650, cy: 100, r: 50, class: "sun" }, svg);
    el("path", { d: "M0 190 Q170 110 340 160 T650 140 T800 160 V420 H0z", class: "hill" }, svg);
    var x = -14, i = 0;
    while (x < 810) {
      var w = 96 + Math.round(rnd() * 46);
      var floors = 3 + Math.round(rnd() * 2);
      var fh = 46, h = floors * fh + 34, y = 420 - h;
      var g = el("g", { class: "facade", style: "--d:" + (i * 0.09).toFixed(2) + "s" }, svg);
      // mansard roof with dormers
      el("path", { d: "M" + (x + 2) + " " + y + " L" + (x + 12) + " " + (y - 30) + " H" + (x + w - 12) + " L" + (x + w - 2) + " " + y + " Z", fill: "#7d8b94" }, g);
      for (var dx = x + 22; dx < x + w - 30; dx += 34) {
        el("path", { d: "M" + dx + " " + (y - 6) + " V" + (y - 22) + " Q" + (dx + 9) + " " + (y - 32) + " " + (dx + 18) + " " + (y - 22) + " V" + (y - 6) + " Z", fill: "#eef1f2" }, g);
      }
      el("rect", { x: x, y: y, width: w, height: h, fill: colors[i % colors.length] }, g);
      el("rect", { x: x - 3, y: y, width: w + 6, height: 7, fill: "rgba(255,255,255,.7)" }, g);
      var cols = w > 120 ? 3 : 2, gap = w / cols;
      for (var r = 0; r < floors; r++) {
        var wy = y + 20 + r * fh;
        for (var c = 0; c < cols; c++) {
          var wx = x + gap * c + gap / 2 - 10;
          el("path", { d: "M" + wx + " " + (wy + 30) + " V" + (wy + 8) + " Q" + (wx + 10) + " " + (wy - 2) + " " + (wx + 20) + " " + (wy + 8) + " V" + (wy + 30) + " Z", fill: "#2a4450" }, g);
          el("rect", { x: wx + 9, y: wy + 2, width: 2, height: 28, fill: "rgba(255,255,255,.35)" }, g);
        }
        if (r > 0 && r < floors) { // balcony rail
          el("rect", { x: x + 6, y: wy + 24, width: w - 12, height: 2.5, fill: "#2b2f33" }, g);
          for (var bx = x + 8; bx < x + w - 8; bx += 7) el("rect", { x: bx, y: wy + 25, width: 1.4, height: 9, fill: "#2b2f33" }, g);
          el("rect", { x: x + 6, y: wy + 33, width: w - 12, height: 2, fill: "#2b2f33" }, g);
        }
      }
      el("path", { d: "M" + (x + w / 2 - 12) + " 420 V" + (420 - 30) + " Q" + (x + w / 2) + " " + (420 - 44) + " " + (x + w / 2 + 12) + " " + (420 - 30) + " V420 Z", fill: "#5b3b2e" }, g);
      x += w - 2; i++;
    }
    palm(svg, 120, 420, 150, false);
    palm(svg, 560, 420, 175, true);
  }
  // Monaco's Rock and the Mediterranean, left half
  function drawSea() {
    var svg = $("#sea"); if (!svg) return;
    palm(svg, 60, 270, 120, false);
  }
  // One coastline from Fréjus to Finale Ligure
  function drawCoast() {
    var path = $("#coastline"), towns = $("#towns"); if (!path || !towns) return;
    var L = path.getTotalLength();
    // [name, position along the coast, class, label above?, line length]
    var list = [
      ["Fréjus", .02, "home", false, 34], ["Cannes", .14, "", true, 34], ["Nice", .3, "", false, 34],
      ["Beausoleil · Monaco", .41, "home", true, 70], ["Roquebrune-Cap-Martin", .455, "home", false, 70],
      ["Menton", .5, "", true, 30], ["Sanremo", .62, "", false, 34], ["Alassio", .8, "", true, 34], ["Finale Ligure", .965, "sister", false, 40]
    ];
    list.forEach(function (t, i) {
      var p = path.getPointAtLength(L * t[1]);
      var dir = t[3] ? -1 : 1, len = t[4];
      var g = el("g", { class: "town " + t[2], style: "--d:" + (0.6 + i * 0.12).toFixed(2) + "s" }, towns);
      el("line", { x1: p.x, y1: p.y, x2: p.x, y2: p.y + dir * len }, g);
      el("circle", { cx: p.x, cy: p.y, r: t[2] ? 8 : 5 }, g);
      var label = el("text", { x: p.x, y: p.y + dir * len + (dir > 0 ? 20 : -10), "text-anchor": i === 0 ? "start" : i === list.length - 1 ? "end" : "middle" }, g);
      label.textContent = t[0];
    });
    // France / Italy border between Menton and Sanremo
    var bp = path.getPointAtLength(L * .53), border = $("#border");
    if (border) {
      var ln = $("line", border); ln.setAttribute("x1", bp.x); ln.setAttribute("x2", bp.x); ln.setAttribute("y2", bp.y);
      $(".b-fr", border).setAttribute("x", bp.x - 10); $(".b-it", border).setAttribute("x", bp.x + 10);
    }
    var fig = $(".coast");
    if (io) { var o = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { fig.classList.add("in"); o.disconnect(); } }, { threshold: .3 }); o.observe(fig); }
    else fig.classList.add("in");
  }

  document.documentElement.classList.remove("no-js");
  document.addEventListener("DOMContentLoaded", function () {
    fillContacts();
    renderGrid("all");
    renderOffers();
    renderItaly();
    initFilters();
    initForm();
    initChrome();
    drawFacades();
    drawSea();
    drawCoast();
    observe($$(".reveal"));
  });
})();
