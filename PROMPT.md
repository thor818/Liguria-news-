# Prompt — Live Riviera

Create a beautiful, modern, magazine-style web newsletter called **"Live Riviera — How to live Liguria & the French Riviera"**.

## Purpose
A monthly newsletter about what happens and what to do in the provinces of **Genoa, Savona and Imperia** (Liguria, Italy) and on the **Côte d'Azur** (French Riviera: Menton, Monaco, Nice, Èze, Villefranche, Cap Ferrat, Cannes). It must link to our website **Riviera Rent** (https://rivierarent.it), so visitors know about food festivals (sagre), celebrations, events, holidays and activities, and can go straight to the organisers' websites and to Riviera Rent to book a holiday home.

## Style
- Modern, elegant, visual, like a travel magazine. People must want to look at it.
- **Very little text**: one short line per item, details on the linked website.
- Large real photos (free-licence photos, e.g. Pexels, with credits), an elegant serif for headings and a clean sans-serif for text.
- Mediterranean colours: sea blue, navy, coral, lemon yellow, warm cream background.
- Light animations (scrolling ticker, hover zoom on photos, sections fading in), respecting "reduced motion".
- Must work perfectly on phones (no horizontal scrolling) and on desktop.

## Languages
At least **6 languages**, switchable from a menu at the top: **Italian, French, English, German, Dutch, Chinese**.
- The page opens in the visitor's browser language and remembers the choice.
- A link parameter (e.g. `?lang=fr`) opens it directly in a language, so each link can open the right language.
- Section titles stay in English as a brand: What's on, Where to go, What to see, What to do, Hiking, Where to eat, Where to stay. Everything else is translated.

## Sections
1. **Cover**: name, issue number and month, short tagline, big photo of the Riviera (e.g. Portofino), counters (upcoming events, places, languages), a scrolling ticker with upcoming events, and an index of all sections.
2. **What's on**: events, food festivals, celebrations, Christmas markets, concerts, culture, sport.
   - 3 featured events in a large photo layout.
   - Agenda cards with photo, date, area, one line of text, a "in X days" countdown and a link to the organiser.
   - Filters by area (Genoa, Savona, Imperia, Côte d'Azur) and by type.
   - Past events disappear automatically.
3. **Where to go**: an illustrated interactive map of the coast from Cannes to Genoa (Italy/France border shown). Tapping an area shows its events.
4. **What to see**: must-see places (Portofino, Genoa old town and Rolli palaces, Promenade des Anglais, Monaco, Menton, Èze, Camogli…), photo tiles linking to Google Maps.
5. **What to do**: experiences in a swipeable carousel (whale watching in the Pelagos Sanctuary, mountain biking in Finale Ligure, snorkelling and diving, beaches, sunset aperitivo, hill villages like Apricale and Dolceacqua).
6. **Hiking**: trails with photo, duration, distance and difficulty (e.g. Portofino → San Fruttuoso, Sentiero del Pellegrino Varigotti–Noli, Riviera dei Fiori cycle path, Cap Ferrat coastal path, Chemin de Nietzsche in Èze, Beigua Park).
7. **Where to eat**: **very important section**.
   - Renowned restaurants (Michelin-starred), traditional restaurants with typical local cuisine, historic street food, pastry shops, filterable by type, with place, price range and a map link (e.g. Mirazur, Le Louis XV, Da Puny, Il Genovese, Antica Sciamadda, Manuelina in Recco, Revello in Camogli, La Merenda, Chez Pipo, Balzola in Alassio).
   - Typical dishes: pesto, focaccia di Recco, farinata/socca, pissaladière, salade niçoise, brandacujun, cappon magro, barbagiuai, Baci di Alassio, Taggiasca olive oil.
   - "Food news": links to the guides that publish reviews and articles on new restaurants (Michelin Guide, Gambero Rosso, Slow Food, Gault&Millau).
8. **Where to stay**: one big card linking to our website **Riviera Rent** (https://rivierarent.it — holiday homes in Liguria; the English version https://rivierarent.it/en/ for all languages except Italian).
9. **Newsletter sign-up**: email form to receive the newsletter every month (to connect to Mailchimp, Brevo or similar).
10. **Footer**: tagline, disclaimer ("dates and programmes may change, always check with the organiser"), photo credits.

## Easy to update
- One simple static website (an `index.html` page plus a `foto/` folder), no complex technology, publishable on any hosting.
- All content (events, places, trails, restaurants, dishes, translations) kept in clearly commented lists at the top of the code, so a non-programmer can update each monthly issue.
- A README explaining how to update it.

## To fill in with real data
- Real events of the month with verified dates and links.
- Check that restaurants are open and the details are correct.
- Our own photos when available.
