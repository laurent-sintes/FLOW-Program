(function () {
  var supportedLanguages = ["fr", "en"];
  var path = window.location.pathname;
  var match = path.match(/^(.*\/)(fr|en)(\/.*)?$/);

  if (!match) {
    return;
  }

  var prefix = match[1];
  var currentLanguage = match[2];
  var pagePath = match[3] || "/";
  var suffix = window.location.search + window.location.hash;

  document.querySelectorAll(".md-select__link[hreflang]").forEach(function (link) {
    var targetLanguage = link.getAttribute("hreflang");

    if (targetLanguage === currentLanguage || supportedLanguages.indexOf(targetLanguage) === -1) {
      return;
    }

    link.href = prefix + targetLanguage + pagePath + suffix;
  });
})();
