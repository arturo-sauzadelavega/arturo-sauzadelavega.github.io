document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".filter-btn");
  const items = document.querySelectorAll(".research-item");

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const filter = this.getAttribute("data-filter");

      buttons.forEach(b => b.classList.remove("active"));
      this.classList.add("active");

      items.forEach(function (item) {
        const tags = item.getAttribute("data-tags");
        if (filter === "all" || tags.includes(filter)) {
          item.classList.remove("hidden");
        } else {
          item.classList.add("hidden");
        }
      });
    });
  });
});
