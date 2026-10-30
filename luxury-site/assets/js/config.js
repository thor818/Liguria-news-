/*
 * Riviera Rent — central site settings.
 * Everything that changes often (contacts, booking link, offers) is edited HERE ONLY,
 * without touching the HTML.
 */
window.FRR_CONFIG = {
  brand: "Riviera Rent",

  // Homes managed (shown in the numbers on the site). Change them here only.
  stats: { homesFR: "45", homesIT: "65" },

  contacts: {
    phone: "+33 (0)4 93 78 86 64",
    phoneHref: "tel:+33493788664",
    mobile: "+33 (0)7 69 27 62 88",
    mobileHref: "tel:+33769276288",
    whatsapp: "33769276288", // number without + or spaces, for wa.me (TO CONFIRM: is WhatsApp on the mobile?)
    email: "info@rivierarent.fr",
    address: "33 Bd du Ténao, 06240 Beausoleil",
    mapsUrl: "https://maps.google.com/?q=33+Boulevard+du+T%C3%A9nao+06240+Beausoleil",
    hours: { en: "Mon–Sat 9:30–12:30 · 14:30–18:00", fr: "Lun–sam 9h30–12h30 · 14h30–18h00" }, // TO CONFIRM
    // Social: paste the full profile address. Empty = icon hidden.
    facebook: "",
    instagram: "",
    youtube: ""
  },

  // Beds24 booking engine (same calendar the channel manager syncs with Booking.com, Airbnb…)
  booking: {
    engineUrl: { en: "https://www.beds24.com/booking2.php?ownerid=15589&lang=en", fr: "https://www.beds24.com/booking2.php?ownerid=15589&lang=fr" },
    // Direct-booking voucher shown on the site (empty = hidden). TO CONFIRM with the office: the old site used 10FRR2020.
    voucher: "10FRR2020"
  },

  /*
   * Sister company in Italy. The section "Also on the Italian Riviera" reads the homes and offers
   * LIVE from rivierarent.it (properties.js and config.js), so prices and offers changed by the
   * Italian office appear here by themselves.
   * featured = ids of the Italian homes to show (in this order) when there is no active offer.
   */
  sister: {
    name: "Riviera Rent",
    url: { en: "https://rivierarent.it/en/", fr: "https://rivierarent.it/en/" },
    dataBase: "https://rivierarent.it",
    featured: ["la-vela", "villa-orizzonte", "al-boschetto", "villa-riders-mansion", "spazio-mare", "palazzo-aycardi"],
    max: 6
  },

  /*
   * OFFERS of the French homes. They appear by themselves between "start" and "end" (YYYY-MM-DD).
   * Same format as the Italian site, plus texts in en / fr / it, so that rivierarent.it can show
   * them too later on. property = id in properties.js; price = "from" price (number only).
   * draft: true = example, NOT shown. Remove "draft: true," when the office has confirmed the price.
   */
  offers: [
    { draft: true, start: "2026-11-01", end: "2027-03-31", property: "la-dragonniere", badge: "-15%", price: "77",
      en: { title: "Winter by the sea", unit: "per night", text: "Mild winter on the Riviera, pool-side apartment near Carnolès beach." },
      fr: { title: "L'hiver au bord de mer", unit: "la nuit", text: "L'hiver doux de la Riviera, appartement côté piscine près de la plage de Carnolès." },
      it: { title: "Inverno al mare", unit: "a notte", text: "L'inverno mite della Costa Azzurra, appartamento sulla piscina vicino alla spiaggia di Carnolès." } }
  ]
};
