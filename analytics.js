"use strict";

(() => {
  // Only measure the live portfolio, never localhost or downloaded previews.
  if (location.hostname !== "yt.jamesboson.com") return;

  const measurementId = "G-HQ7TTCGWDC";
  const cloudflareToken = "2070b01ba4b5413dbd8041bf75dda671";

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () {
    window.dataLayer.push(arguments);
  };
  window.gtag("js", new Date());
  window.gtag("config", measurementId, {
    allow_google_signals: false,
    allow_ad_personalization_signals: false,
  });

  const googleTag = document.createElement("script");
  googleTag.async = true;
  googleTag.src = `https://www.googletagmanager.com/gtag/js?id=${measurementId}`;
  document.head.append(googleTag);

  if (cloudflareToken) {
    const beacon = document.createElement("script");
    beacon.type = "module";
    beacon.src = "https://static.cloudflareinsights.com/beacon.min.js";
    beacon.setAttribute(
      "data-cf-beacon",
      JSON.stringify({ token: cloudflareToken, spa: false }),
    );
    document.body.append(beacon);
  }

  // Track the intent to open a film; this does not claim playback has started.
  // Only public video IDs and fixed UI labels are sent in these custom events.
  document.addEventListener("click", (event) => {
    const target = event.target.closest("a, button");
    if (!target) return;

    const parameters = { site_language: document.documentElement.lang };
    if (target.matches("[data-video]")) {
      window.gtag("event", "film_open", {
        ...parameters,
        video_id: target.dataset.video,
        placement: target.matches(".hero-play") ? "hero" : "gallery",
      });
    } else if (target.matches("[data-filter]")) {
      window.gtag("event", "work_filter", {
        ...parameters,
        work_category: target.dataset.filter,
      });
    } else if (target.matches("a[href^='https://www.instagram.com/jbs.street.recordings/']")) {
      window.gtag("event", "contact_click", {
        ...parameters,
        contact_method: "instagram",
        placement: target.closest("section")?.id || "footer",
      });
    }
  });
})();
