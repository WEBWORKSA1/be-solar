/* Be.Solar — site behaviour. Vanilla JS, no dependencies. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- Contact routing (address is assembled at runtime, never written in the page) ---------- */
  function inbox() {
    var p = ["MWFza3Jvd2Jldw==", "bW9jLmxpYW1n"]; // reversed + encoded
    var rev = function (s) { return s.split("").reverse().join(""); };
    return rev(atob(p[0])) + String.fromCharCode(64) + rev(atob(p[1]));
  }
  window.BeSolar = window.BeSolar || {};

  /* Any element with [data-mail] opens the visitor's mail app on click */
  $$("[data-mail]").forEach(function (a) {
    a.setAttribute("href", "#contact");
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var subj = encodeURIComponent(a.getAttribute("data-mail") || "Be.Solar inquiry");
      window.location.href = "mai" + "lto:" + inbox() + "?subject=" + subj;
    });
  });

  /* ---------- Theme ---------- */
  var root = document.documentElement;
  try { var t = localStorage.getItem("bs-theme"); if (t) root.setAttribute("data-theme", t); } catch (e) {}
  var tb = $(".theme-btn");
  if (tb) tb.addEventListener("click", function () {
    var dark = root.getAttribute("data-theme") === "dark" ||
      (!root.getAttribute("data-theme") && window.matchMedia("(prefers-color-scheme: dark)").matches);
    var next = dark ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("bs-theme", next); } catch (e) {}
  });

  /* ---------- Mobile menu ---------- */
  var mb = $(".menu-btn"), nav = $(".nav");
  if (mb && nav) mb.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    mb.setAttribute("aria-expanded", open ? "true" : "false");
  });

  /* ---------- Consent notice ---------- */
  var c = $(".consent");
  try { if (c && !localStorage.getItem("bs-consent")) c.classList.add("show"); } catch (e) { if (c) c.classList.add("show"); }
  $$("[data-consent]").forEach(function (b) {
    b.addEventListener("click", function () {
      try { localStorage.setItem("bs-consent", b.getAttribute("data-consent")); } catch (e) {}
      if (b.getAttribute("data-consent") === "essential") { (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1; }
      c.classList.remove("show");
    });
  });

  /* ---------- YouTube click-to-load ---------- */
  $$(".yt-facade").forEach(function (b) {
    var id = b.getAttribute("data-yt");
    b.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
    b.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      f.title = b.getAttribute("aria-label") || "Video";
      f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      b.parentNode.replaceChild(f, b);
    });
  });

  /* ---------- Forms: every .js-form posts to the inbox through FormSubmit ---------- */
  function serialize(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) {
      if (data[k]) data[k] = data[k] + ", " + v; else data[k] = v;
    });
    return data;
  }
  function showMsg(form, ok, text) {
    var m = $(".form-msg", form.parentNode) || $(".form-msg", form);
    if (!m) return;
    m.className = "form-msg " + (ok ? "ok" : "err");
    m.textContent = text;
    m.setAttribute("role", ok ? "status" : "alert");
    m.scrollIntoView({ block: "nearest" });
  }
  function send(form, extra) {
    var data = serialize(form);
    if (data._honey) return Promise.resolve(true); // bot
    delete data._honey;
    Object.keys(extra || {}).forEach(function (k) { data[k] = extra[k]; });
    data._subject = "[Be.Solar] " + (form.getAttribute("data-subject") || "Website form");
    data._template = "table";
    data._captcha = "false";
    data.page = location.href;
    return fetch("https://formsubmit.co/ajax/" + inbox(), {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(data)
    }).then(function (r) { return r.ok; }).catch(function () { return false; });
  }
  BeSolar.send = send;
  $$("form.js-form").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = $("[type=submit]", form); if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = "Sending…"; }
      send(form).then(function (ok) {
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; }
        if (ok) { showMsg(form, true, form.getAttribute("data-ok") || "Received. We'll reply within two business days."); form.reset(); }
        else showMsg(form, false, "That didn't go through. Check your connection and send it again.");
      });
    });
  });

  /* ---------- Solar model (shared by the hero dial, calculators and the quote wizard) ---------- */
  var COUNTRIES = {
    US: { name: "United States", cur: "USD", sym: "$", rate: 0.18, sun: 4.6, cpw: 2.7, co2: 0.37, esc: 0.03, billMax: 600, bill: 160 },
    CA: { name: "Canada", cur: "CAD", sym: "C$", rate: 0.17, sun: 3.9, cpw: 2.8, co2: 0.11, esc: 0.03, billMax: 500, bill: 150 },
    UK: { name: "United Kingdom", cur: "GBP", sym: "£", rate: 0.26, sun: 2.7, cpw: 1.7, co2: 0.18, esc: 0.03, billMax: 400, bill: 110 },
    AU: { name: "Australia", cur: "AUD", sym: "A$", rate: 0.33, sun: 4.6, cpw: 1.1, co2: 0.6, esc: 0.03, billMax: 700, bill: 200 },
    IN: { name: "India", cur: "INR", sym: "₹", rate: 7, sun: 4.5, cpw: 60, co2: 0.71, esc: 0.03, billMax: 20000, bill: 3000 },
    XX: { name: "Other country", cur: "USD", sym: "$", rate: 0.2, sun: 4.5, cpw: 2.5, co2: 0.45, esc: 0.03, billMax: 600, bill: 150 }
  };
  BeSolar.COUNTRIES = COUNTRIES;
  var PANEL_W = 430, PR = 0.8, LIFE = 25, DEG = 0.005;

  /* India PM Surya Ghar residential subsidy: per-kW on first 2 kW, reduced for the 3rd kW, capped above 3 kW */
  function subsidy(country, kw) {
    if (country === "IN") {
      var s = Math.min(kw, 2) * 30000 + Math.max(0, Math.min(kw, 3) - 2) * 18000;
      return Math.min(s, 78000);
    }
    return 0;
  }

  function model(o) {
    var c = COUNTRIES[o.country] || COUNTRIES.US;
    var rate = o.rate || c.rate, sun = o.sun || c.sun, cpw = o.cpw || c.cpw;
    var offset = (o.offset == null ? 100 : o.offset) / 100;
    var annualKwh = (o.bill * 12) / rate;
    var target = annualKwh * offset;
    var kw = target / (sun * 365 * PR);
    kw = Math.max(1, Math.round(kw * 10) / 10);
    var panels = Math.ceil(kw * 1000 / PANEL_W);
    var gross = kw * 1000 * cpw;
    var sub = subsidy(o.country, kw);
    var credit = gross * ((o.creditPct || 0) / 100);
    var net = Math.max(0, gross - sub - credit - (o.rebate || 0));
    var prod = kw * sun * 365 * PR;
    var esc = o.esc == null ? c.esc : o.esc / 100;
    var cum = -net, payback = null, total = 0, series = [];
    for (var y = 1; y <= LIFE; y++) {
      var save = Math.min(prod * Math.pow(1 - DEG, y - 1), annualKwh) * rate * Math.pow(1 + esc, y - 1);
      total += save; cum += save; series.push(cum);
      if (payback === null && cum >= 0) payback = y - 1 + (save - cum) / save;
    }
    return {
      c: c, kw: kw, panels: panels, gross: gross, subsidy: sub, credit: credit, net: net,
      prodYr1: prod, annualKwh: annualKwh, save1: Math.min(prod, annualKwh) * rate,
      save25: total, net25: total - net, payback: payback, series: series,
      roofM2: panels * 2.0, co2t: prod * LIFE * c.co2 / 1000,
      roi: net > 0 ? ((total - net) / net) * 100 : 0
    };
  }
  BeSolar.model = model;

  function money(v, c, compact) {
    var opts = { style: "currency", currency: c.cur, maximumFractionDigits: 0 };
    if (compact && Math.abs(v) >= 100000) { opts.notation = "compact"; opts.maximumFractionDigits = 1; }
    try { return new Intl.NumberFormat(c.cur === "INR" ? "en-IN" : "en", opts).format(v); }
    catch (e) { return c.sym + Math.round(v).toLocaleString(); }
  }
  BeSolar.money = money;
  function num(v, d) { return Number(v).toLocaleString("en", { maximumFractionDigits: d || 0 }); }

  /* ---------- Hero sun dial ---------- */
  var dial = $("#dial");
  if (dial) {
    var dc = $("#dial-country"), ds = $("#dial-bill");
    var arc = $(".sun-dot", dial);
    function drawDial() {
      var c = COUNTRIES[dc.value];
      var max = c.billMax;
      if (+ds.max !== max) { ds.min = Math.round(max * 0.04 / 10) * 10; ds.max = max; ds.step = max > 2000 ? 100 : 5; ds.value = c.bill; }
      var bill = +ds.value;
      var m = model({ country: dc.value, bill: bill });
      $("#dial-bill-out").textContent = money(bill, c);
      $("#dial-kw").textContent = num(m.kw, 1) + " kW";
      $("#dial-panels").textContent = m.panels;
      $("#dial-save").textContent = money(m.net25, c, true);
      var t = (bill - +ds.min) / (max - +ds.min); // 0..1 along the arc
      var ang = Math.PI * (1 - t);
      var x = 200 + 160 * Math.cos(ang), y = 190 - 160 * Math.sin(ang);
      arc.setAttribute("transform", "translate(" + x.toFixed(1) + " " + y.toFixed(1) + ")");
      var q = $("#dial-quote"); if (q) q.href = q.getAttribute("data-base") + "?country=" + dc.value + "&bill=" + bill;
    }
    dc.addEventListener("change", function () { ds.max = 0; drawDial(); });
    ds.addEventListener("input", drawDial);
    ds.max = 0; drawDial();
  }

  /* ---------- Calculators ---------- */
  function chart(el, series, c) {
    var w = 560, h = 200, pad = 34, n = series.length;
    var min = Math.min(0, Math.min.apply(null, series)), max = Math.max(1, Math.max.apply(null, series));
    var x = function (i) { return pad + (i / (n - 1)) * (w - pad - 8); };
    var y = function (v) { return 10 + (1 - (v - min) / (max - min)) * (h - 40); };
    var bars = series.map(function (v, i) {
      var y0 = y(0), y1 = y(v), bw = (w - pad - 8) / n - 3;
      return '<rect x="' + (x(i) - bw / 2).toFixed(1) + '" y="' + Math.min(y0, y1).toFixed(1) + '" width="' + bw.toFixed(1) + '" height="' + Math.max(1, Math.abs(y1 - y0)).toFixed(1) + '" rx="2" fill="' + (v < 0 ? "var(--cell)" : "var(--leaf)") + '"><title>Year ' + (i + 1) + ": " + money(v, c) + "</title></rect>";
    }).join("");
    el.innerHTML = '<svg viewBox="0 0 ' + w + " " + h + '" role="img" aria-label="Cumulative net savings by year"><line x1="' + pad + '" x2="' + (w - 8) + '" y1="' + y(0) + '" y2="' + y(0) + '" stroke="var(--line)"/>' + bars +
      '<text x="' + pad + '" y="' + (h - 8) + '" font-size="12" fill="var(--muted)">Year 1</text><text x="' + (w - 8) + '" y="' + (h - 8) + '" font-size="12" text-anchor="end" fill="var(--muted)">Year 25</text>' +
      '<text x="4" y="' + (y(0) + 4) + '" font-size="11" fill="var(--muted)">0</text></svg>';
  }

  $$("form.calc-form").forEach(function (f) {
    var kind = f.getAttribute("data-calc");
    var out = $("#" + f.getAttribute("data-out"));
    function presets() {
      var c = COUNTRIES[f.country.value];
      $$("[data-cur]", f).forEach(function (s) { s.textContent = c.sym; });
      if (f.rate) f.rate.value = c.rate;
      if (f.sun) f.sun.value = c.sun;
      if (f.cpw) f.cpw.value = c.cpw;
      if (f.bill) f.bill.value = c.bill;
    }
    function run() {
      var c = COUNTRIES[f.country.value];
      var g = function (n) { return f[n] ? parseFloat(f[n].value) : undefined; };
      if (kind === "battery") {
        var daily = g("daily"), hours = g("hours"), crit = g("critical") / 100, dod = g("dod") / 100;
        var need = daily * crit * (hours / 24) / dod;
        var units = Math.ceil(need / g("unit"));
        $("[data-o=kwh]", out).textContent = num(need, 1) + " kWh";
        $("[data-o=units]", out).textContent = units + (units === 1 ? " battery" : " batteries");
        $("[data-o=cost]", out).textContent = money(units * g("unit") * g("perkwh"), c);
        $("[data-o=power]", out).textContent = num(daily * crit / 24 * 2.5, 1) + " kW";
        return;
      }
      var m = model({
        country: f.country.value, bill: g("bill"), rate: g("rate"), sun: g("sun"), cpw: g("cpw"),
        offset: g("offset"), creditPct: g("credit") || 0, rebate: g("rebate") || 0, esc: g("esc")
      });
      var set = function (k, v) { var el = $("[data-o=" + k + "]", out); if (el) el.textContent = v; };
      set("save25", money(m.net25, c));
      set("save1", money(m.save1, c));
      set("kw", num(m.kw, 1) + " kW");
      set("panels", m.panels + " × " + PANEL_W + " W");
      set("gross", money(m.gross, c));
      set("net", money(m.net, c));
      set("subsidy", money(m.subsidy + m.credit + (g("rebate") || 0), c));
      set("payback", m.payback == null ? "Over 25 years" : num(m.payback, 1) + " years");
      set("prod", num(m.prodYr1) + " kWh/yr");
      set("roof", num(m.roofM2) + " m² (" + num(m.roofM2 * 10.764) + " ft²)");
      set("co2", num(m.co2t, 1) + " tonnes");
      set("roi", num(m.roi) + "%");
      var ch = $(".chart", out); if (ch) chart(ch, m.series, c);
      var q = $("[data-quote-link]", out); if (q) q.href = q.getAttribute("data-base") + "?country=" + f.country.value + "&bill=" + g("bill");
    }
    if (f.country) f.country.addEventListener("change", function () { presets(); run(); });
    f.addEventListener("input", run);
    f.addEventListener("submit", function (e) { e.preventDefault(); run(); });
    if (f.country) presets();
    run();
  });

  /* ---------- Quote wizard ---------- */
  var wiz = $("#quote-wizard");
  if (wiz) {
    var steps = $$(".step", wiz), i = 0, bar = $(".progress i", wiz.parentNode);
    var qs = new URLSearchParams(location.search);
    if (qs.get("country") && wiz.country) wiz.country.value = qs.get("country");
    var wb = wiz.bill;
    function syncBill() {
      var c = COUNTRIES[wiz.country.value] || COUNTRIES.US;
      wb.min = Math.round(c.billMax * 0.04 / 10) * 10; wb.max = c.billMax; wb.step = c.billMax > 2000 ? 100 : 5;
      $("#wiz-bill-out").textContent = money(+wb.value, c);
      var m = model({ country: wiz.country.value, bill: +wb.value });
      $("#live-kw").textContent = num(m.kw, 1) + " kW";
      $("#live-panels").textContent = m.panels;
      $("#live-save1").textContent = money(m.save1, c);
      $("#live-save25").textContent = money(m.net25, c, true);
      $("#live-co2").textContent = num(m.co2t, 1) + " t";
    }
    if (qs.get("bill")) wb.value = qs.get("bill");
    else wb.value = (COUNTRIES[wiz.country.value] || COUNTRIES.US).bill;
    wiz.country.addEventListener("change", function () { wb.value = (COUNTRIES[wiz.country.value] || COUNTRIES.US).bill; syncBill(); });
    wb.addEventListener("input", syncBill);
    syncBill();

    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle("on", k === n); });
      i = n;
      if (bar) bar.style.width = ((n + 1) / steps.length * 100) + "%";
      $("#wiz-count").textContent = "Step " + (n + 1) + " of " + steps.length;
      $("#wiz-back").style.visibility = n === 0 ? "hidden" : "visible";
      $("#wiz-next").hidden = n === steps.length - 1;
      $("#wiz-submit").hidden = n !== steps.length - 1;
      var h = $("h2", steps[n]); if (h && n > 0) { h.setAttribute("tabindex", "-1"); h.focus(); }
    }
    function valid(n) {
      var ok = true;
      $$("input,select,textarea", steps[n]).forEach(function (el) {
        if (!el.checkValidity()) { if (ok) el.reportValidity(); ok = false; }
      });
      return ok;
    }
    $("#wiz-next").addEventListener("click", function () { if (valid(i)) show(i + 1); });
    $("#wiz-back").addEventListener("click", function () { show(Math.max(0, i - 1)); });
    wiz.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!valid(i)) return;
      var m = model({ country: wiz.country.value, bill: +wb.value });
      var sbtn = $("#wiz-submit"); sbtn.disabled = true; sbtn.textContent = "Sending…";
      send(wiz, { est_system_kw: m.kw, est_panels: m.panels, est_year1_savings: Math.round(m.save1), lead_score: score() }).then(function (ok) {
        sbtn.disabled = false; sbtn.textContent = "Get my free quotes";
        if (ok) {
          wiz.hidden = true; $(".wiz-meta").hidden = true;
          var d = $("#wiz-done"); d.hidden = false; d.focus();
        } else showMsg(wiz, false, "That didn't go through. Check your connection and press Get my free quotes again.");
      });
    });
    function score() {
      var s = 0, v = function (n) { var el = wiz.querySelector("[name='" + n + "']:checked") || wiz[n]; return el ? el.value : ""; };
      if (v("ownership") === "Own") s += 30;
      if (v("timeline") === "Within 3 months") s += 25; else if (v("timeline") === "3–6 months") s += 15;
      if (v("shade") === "No shade" || v("shade") === "Light shade") s += 15;
      if (+wb.value >= (COUNTRIES[wiz.country.value] || COUNTRIES.US).bill) s += 15;
      if (v("credit_band") === "Excellent (720+)" || v("credit_band") === "Good (660–719)" || v("financing") === "Cash") s += 15;
      return s >= 70 ? "Hot (" + s + ")" : s >= 45 ? "Warm (" + s + ")" : "Nurture (" + s + ")";
    }
    show(0);
  }

  /* ---------- Donation amount picker ---------- */
  $$(".tier [data-amount]").forEach(function (b) {
    b.addEventListener("click", function () {
      var f = $("#pledge-form");
      if (f) { f.amount.value = b.getAttribute("data-amount"); f.tier.value = b.getAttribute("data-tier"); f.scrollIntoView({ behavior: "smooth" }); f.amount.focus(); }
    });
  });

  /* ---------- Year ---------- */
  $$("[data-year]").forEach(function (e) { e.textContent = new Date().getFullYear(); });
})();
