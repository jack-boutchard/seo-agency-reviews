/* SEO Agency Reviews — progressive enhancement only.
   The site is fully functional with this file absent or disabled.
   No content is rendered here; this only enhances existing HTML. */
(function () {
  "use strict";

  /* Mobile nav toggle */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* Optional click-to-sort on tables marked data-sortable.
     Tables are fully readable without this; it only reorders rows. */
  function cellValue(row, idx) {
    var cell = row.children[idx];
    if (!cell) return "";
    var raw = cell.getAttribute("data-sort") || cell.textContent || "";
    var num = parseFloat(raw.replace(/[^0-9.\-]/g, ""));
    return isNaN(num) ? raw.trim().toLowerCase() : num;
  }

  document.querySelectorAll("table[data-sortable]").forEach(function (table) {
    var headers = table.querySelectorAll("thead th");
    headers.forEach(function (th, idx) {
      if (th.hasAttribute("data-nosort")) return;
      th.classList.add("sortable");
      var label = th.textContent;
      th.innerHTML = "";
      var btn = document.createElement("button");
      btn.type = "button";
      btn.textContent = label;
      th.appendChild(btn);
      var dir = 1;
      btn.addEventListener("click", function () {
        var tbody = table.querySelector("tbody");
        var rows = Array.prototype.slice.call(tbody.querySelectorAll("tr"));
        rows.sort(function (a, b) {
          var va = cellValue(a, idx), vb = cellValue(b, idx);
          if (va < vb) return -1 * dir;
          if (va > vb) return 1 * dir;
          return 0;
        });
        rows.forEach(function (r) { tbody.appendChild(r); });
        headers.forEach(function (h) { h.removeAttribute("aria-sort"); });
        th.setAttribute("aria-sort", dir === 1 ? "ascending" : "descending");
        dir *= -1;
      });
    });
  });
})();
