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

## Two coasts, separate or together
At the top of the page and right under the cover, the reader chooses **Liguria**, **Côte d'Azur** or **Both**, with two big photo buttons and a third "Both" button, plus a small switch always visible in the top bar. All sections (events, map, places, experiences, hiking, restaurants, dishes) then show only the chosen coast, so the information is never mixed up. Direct links open one coast (e.g. `?region=liguria`, `?region=azur`), and can be combined with the language.

## Languages
At least **6 languages**, switchable from a menu at the top: **Italian, French, English, German, Dutch, Chinese**.
- The page opens in the visitor's browser language and remembers the choice.
- A link parameter (e.g. `?lang=fr`) opens it directly in a language, so each link can open the right language.
- Section titles stay in English as a brand: What's on, Where to go, What to see, What to do, Hiking, Where to eat, Where to stay. Everything else is translated.

## Sections
Keep it simple, with few big sections, like the menu of the Cannes tourism website (Explorer · Que faire · Où manger · Où dormir · Agenda). A "Menu" button opens a full-screen menu with only these five big entries and arrows, plus links to Riviera Rent and the newsletter.

1. **Cover**: name, issue number and month, short tagline, big photo (Portofino for Liguria, Nice for the Côte d'Azur), small counters, then **"Choose your Riviera"**: Liguria / Côte d'Azur / Both.
2. **Explore**: must-see places as photo tiles linking to Google Maps (Portofino, Genoa old town, Genoa by the sea, Camogli, Promenade des Anglais, Monaco, Menton, Èze) and an illustrated interactive map of the coast from Cannes to Genoa; tapping an area shows its events.
3. **What to do**: experiences in a swipeable carousel (whale watching in the Pelagos Sanctuary, mountain biking in Finale Ligure, diving, beaches, sunset aperitivo, Monaco from above, hill villages) plus canyoning and trail running on the Côte d'Azur; each experience links to the official websites, and a **"Book an activity"** box links to them too: for the Côte d'Azur **cotedazurfrance.fr** (official site, English version cotedazurfrance.com) and **experiencecotedazur.com** (book sport and adventure activities, English version en.experiencecotedazur.com); for Liguria **lamialiguria.it** (official Liguria website). Then **Hiking trails** with photo, duration, distance and difficulty (Portofino → San Fruttuoso, Sentiero del Pellegrino, Riviera dei Fiori cycle path, Cap Ferrat coastal path, Chemin de Nietzsche, Beigua Park).
4. **Where to eat**: **very important**. Renowned and Michelin-starred restaurants, traditional local cuisine, historic street food and pastry shops, filterable by type, with place, price range and map link (Mirazur, Le Louis XV, Da Puny, Il Genovese, Antica Sciamadda, Manuelina, Revello, La Merenda, Chez Pipo, Balzola, L'Alchimie in Nice, L'Orangerie in Menton); typical dishes of each coast (pesto, focaccia di Recco, farinata/socca, brandacujun, cappon magro, barbagiuai, Baci di Alassio, Taggiasca oil, pissaladière, salade niçoise, pan bagnat, tourte de blettes, barbajuan); "Food news" links to the guides that review new restaurants (Michelin, Gambero Rosso, Slow Food, Gault&Millau, Tripadvisor).
5. **Where to stay**: one big card linking to our website **Riviera Rent** (https://rivierarent.it — holiday homes in Liguria; https://rivierarent.it/en/ for all languages except Italian).
6. **What's on** (agenda): food festivals, celebrations, Christmas markets, concerts, culture, sport; 3 featured events in a large photo layout, then cards with photo, date, area, one line, an "in X days" countdown and a link to the organiser; filters by area and type; past events disappear automatically.
7. **Newsletter sign-up** and **footer** with disclaimer and photo credits.

## Easy to update
- One simple static website (an `index.html` page plus a `foto/` folder), no complex technology, publishable on any hosting.
- All content (events, places, trails, restaurants, dishes, translations) kept in clearly commented lists at the top of the code, so a non-programmer can update each monthly issue.
- A README explaining how to update it.

## To fill in with real data
- Real events of the month with verified dates and links.
- Check that restaurants are open and the details are correct.
- Our own photos when available.
