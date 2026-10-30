# Live Riviera — How to live Liguria & the French Riviera

Giornalino web in 6 lingue (italiano, français, English, Deutsch, Nederlands, 中文) con gli eventi di Genova, Savona, Imperia e Costa Azzurra.
La pagina è `index.html`, le foto sono nella cartella `foto/`. Si apre con qualsiasi browser e si pubblica su qualsiasi hosting.

## Liguria o Costa Azzurra

In alto e sotto la copertina il lettore sceglie **Liguria**, **Costa Azzurra** o **tutte e due**: eventi, mappa, luoghi, esperienze, sentieri, ristoranti e piatti mostrano solo la costa scelta.
Link diretti: `?region=liguria` oppure `?region=azur` (si possono unire alla lingua: `?region=azur&lang=fr`).
Le esperienze (`TODO`) e i piatti (`DISHES`) hanno il campo costa: `lig`, `azur` o `both`; le altre voci usano `zone`.

## Le rubriche

Cinque rubriche, raggiungibili anche dal menu a schermo intero (pulsante ☰ in alto):

| Rubrica | Cosa contiene | Dove si modifica in `index.html` |
|---|---|---|
| Explore | luoghi da vedere, Genova in evidenza, 40 City guides (da vedere, musei, da fare, dove mangiare, sapori), Artists' Riviera e mappa | `SEE`, `CITIES`, `ARTISTS`, `PINS` |
| What to do | esperienze, "Book an activity", Sport & adventure, Family fun e sentieri (Hiking) | `TODO`, `SITES`, `SPORTS`, `FAMILY`, `HIKES` |
| Where to eat | ristoranti, piatti tipici, guide gastronomiche | `RESTAURANTS`, `DISHES`, `GUIDES` |
| Where to stay | link a Riviera Rent | sezione `#stay`, `SITE_IT` |
| What's on | agenda: eventi, sagre, feste | `EVENTS` |

## Come aggiornarlo per un nuovo numero

Tutti i contenuti sono in cima allo `<script>` di `index.html`, sotto **CONTENUTI**.

- Ogni voce ha `t` con i testi nelle 6 lingue (`it`, `fr`, `en`, `de`, `nl`, `zh`); se una lingua manca si usa l'inglese.
- `zone`: `genova` | `savona` | `imperia` | `azur`
- `img`: foto nella cartella `foto/`; se vuota si usa un'illustrazione con l'emoji.
- Eventi: `date` / `end` in formato `AAAA-MM-GG`; `featured: 1/2/3` per il primo piano. Gli eventi finiti spariscono da soli.
- Luoghi, sentieri e ristoranti: `q` è la ricerca che apre Google Maps.
- Ristoranti: `tag` = `michelin` | `modern` | `trad` | `street` | `sweet`, `price` da `€` a `€€€€` (il filtro per prezzo usa € = economico, €€ = medio, €€€ e oltre = alto livello).
- Siti ufficiali e di prenotazione (lamialiguria.it, cotedazurfrance.fr, experiencecotedazur.com): oggetto `SITES`, con l'indirizzo per ogni lingua (`other` = versione inglese).
- City guides (`CITIES`): per aggiungere un posto basta scriverne il nome nella lista `see`, `museums` o `eat` della città (oppure `do` per le cose da fare, `taste` per sapori e prodotti tipici); il link a Google Maps si crea da solo. Genova è messa in evidenza in Explore e la sua guida si apre per prima.
- Testi dell'interfaccia: oggetto `I18N`, una sezione per lingua.

## Da completare

- Il link a Riviera Rent è in `SITE_IT` (italiano → rivierarent.it, altre lingue → rivierarent.it/en/).
- Iscrizione newsletter: collegare il `<form>` al vostro servizio (Mailchimp, Brevo, ...).
- Gli eventi del N° 1 sono esempi: verificare date e link prima di pubblicare.
- Ristoranti, tempi e distanze dei sentieri: verificare prima di pubblicare.

## Collegamento dai vostri siti

Aggiungere `?lang=` all'indirizzo per aprire il giornalino già nella lingua giusta:
`it`, `fr`, `en`, `de`, `nl`, `zh` (es. `https://<indirizzo>/index.html?lang=de`).
Senza parametro si usa la lingua del browser del visitatore.

## Foto

Le foto vengono da [Pexels](https://www.pexels.com) e si usano gratis, anche per scopi commerciali ([licenza Pexels](https://www.pexels.com/license/)).
L'elenco con il link a ogni foto è in `foto/CREDITI.md`. Se aggiungete una foto, mettetela in `foto/` e scrivete il percorso nel campo `img`.
