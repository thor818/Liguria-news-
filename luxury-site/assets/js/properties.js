/*
 * List of homes. To add or change a home, edit only this file. Fields:
 *  id, name, town, area (monaco | roquebrune | frejus),
 *  guests, bedrooms (0 = studio), bathrooms,
 *  pool, seaView, parking, shortTerm (holiday lets), longTerm (6+ months),
 *  fromPrice: "from € … / night" (number only; empty = not shown),
 *  photos: number of photos in /assets/img/homes/<id>/01.jpg, 02.jpg… (cover.jpg = card picture),
 *  bookingUrl: page of the home on Beds24 (empty = list of all homes),
 *  tag { en, fr }: short highlight; desc { en, fr }.
 *
 * NB: data copied from the old site (frenchrivierarent.com, 2020).
 * The office should check guests, prices and registration numbers before going live.
 */
window.FRR_PROPERTIES = [
  {
    id: "kristal-palace", name: "Kristal Palace", town: "Beausoleil", area: "monaco",
    guests: 4, bedrooms: 1, bathrooms: 1, pool: true, seaView: true, parking: true, shortTerm: true, longTerm: true,
    fromPrice: "", photos: 29, bookingUrl: "",
    tag: { en: "Indoor pool · hot tub", fr: "Piscine intérieure · jacuzzi" },
    desc: {
      en: "Air-conditioned apartment 1.2 km from the Grimaldi Forum, with terrace, hot tub and access to the residence's indoor pool.",
      fr: "Appartement climatisé à 1,2 km du Grimaldi Forum, avec terrasse, jacuzzi et accès à la piscine intérieure de la résidence."
    }
  },
  {
    id: "elidia-palace", name: "Elidia Palace", town: "Beausoleil", area: "monaco",
    guests: 2, bedrooms: 2, bathrooms: 2, pool: false, seaView: true, parking: true, shortTerm: true, longTerm: true,
    fromPrice: "", photos: 21, bookingUrl: "",
    tag: { en: "Sea-view balcony", fr: "Balcon vue mer" },
    desc: {
      en: "Bright apartment with balcony and terrace, 2 bedrooms and 2 bathrooms, 400 m from Pont de Fer beach.",
      fr: "Appartement lumineux avec balcon et terrasse, 2 chambres et 2 salles de bains, à 400 m de la plage du Pont de Fer."
    }
  },
  {
    id: "palais-josephine", name: "Palais Joséphine 411", town: "Beausoleil", area: "monaco",
    guests: 3, bedrooms: 0, bathrooms: 1, pool: true, seaView: false, parking: true, shortTerm: true, longTerm: true,
    fromPrice: "", photos: 14, bookingUrl: "",
    tag: { en: "Belle Époque palace", fr: "Palais Belle Époque" },
    desc: {
      en: "Cosy studio in a Belle Époque palace less than 1 km from Monaco, with terrace and seasonal outdoor pool.",
      fr: "Studio cosy dans un palais Belle Époque à moins d'1 km de Monaco, avec terrasse et piscine extérieure en saison."
    }
  },
  {
    id: "monte-carlo-view", name: "Monte Carlo View", town: "Beausoleil", area: "monaco",
    guests: 6, bedrooms: 2, bathrooms: 1, pool: false, seaView: true, parking: true, shortTerm: false, longTerm: true,
    fromPrice: "", photos: 11, bookingUrl: "",
    tag: { en: "Long stays", fr: "Longue durée" },
    desc: {
      en: "Two-bedroom apartment with terrace and washing machine, 300 m from Pont de Fer beach. Available for long stays.",
      fr: "Deux-pièces avec terrasse et lave-linge, à 300 m de la plage du Pont de Fer. Disponible en location longue durée."
    }
  },
  {
    id: "la-dragonniere", name: "La Dragonnière", town: "Roquebrune-Cap-Martin", area: "roquebrune",
    guests: 4, bedrooms: 2, bathrooms: 2, pool: true, seaView: true, parking: true, shortTerm: true, longTerm: true,
    fromPrice: "90", photos: 19, bookingUrl: "",
    tag: { en: "Pool & garden", fr: "Piscine & jardin" },
    desc: {
      en: "2 bedrooms, 2 bathrooms and a balcony over the pool, in a residence with garden near Carnolès beach.",
      fr: "2 chambres, 2 salles de bains et un balcon sur la piscine, dans une résidence avec jardin près de la plage de Carnolès."
    }
  },
  {
    id: "villa-gabriella", name: "Villa Gabriella", town: "Roquebrune-Cap-Martin", area: "roquebrune",
    guests: 4, bedrooms: 1, bathrooms: 1, pool: true, seaView: true, parking: true, shortTerm: true, longTerm: true,
    fromPrice: "", photos: 18, bookingUrl: "",
    tag: { en: "Private pool", fr: "Piscine privée" },
    desc: {
      en: "Garden apartment with private pool and terrace, between Cap-Martin and the beaches of Carnolès.",
      fr: "Appartement en rez-de-jardin avec piscine privée et terrasse, entre le Cap-Martin et les plages de Carnolès."
    }
  },
  {
    id: "logis-de-valescure", name: "Les Logis de Valescure", town: "Fréjus", area: "frejus",
    guests: 8, bedrooms: 2, bathrooms: 2, pool: false, seaView: false, parking: true, shortTerm: true, longTerm: true,
    fromPrice: "85", photos: 24, bookingUrl: "",
    tag: { en: "Historic residence · garden", fr: "Résidence historique · jardin" },
    desc: {
      en: "Large apartment in a grand old residence in Valescure, with terrace and park. 24 km from Cannes.",
      fr: "Grand appartement dans une belle résidence ancienne de Valescure, avec terrasse et parc. À 24 km de Cannes."
    }
  }
];
