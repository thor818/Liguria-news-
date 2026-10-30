# La Riviera — il giornalino degli eventi

Giornalino web in 6 lingue (italiano, français, English, Deutsch, Nederlands, 中文) con gli eventi di Genova, Savona, Imperia e Costa Azzurra.
La pagina è `index.html`, le foto sono nella cartella `foto/`. Si apre con qualsiasi browser e si pubblica su qualsiasi hosting.

## Come aggiornarlo per un nuovo numero

Apri `index.html` e cerca **CONTENUTI DEL GIORNALINO**:

- `ISSUE` — numero e mese dell'edizione.
- `EVENTS` — gli eventi. Ogni evento ha:
  - `zone`: `genova` | `savona` | `imperia` | `azur`
  - `cat`: `sagre` | `feste` | `musica` | `mercatini` | `cultura` | `sport`
  - `date`: data di inizio `AAAA-MM-GG` (serve per l'ordine e il badge)
  - `icon`: un'emoji
  - `t`: per ogni lingua (`it`, `fr`, `en`, `de`, `nl`, `zh`) titolo, luogo e una frase breve. Se una lingua manca si usa l'inglese.
  - `end`: data di fine (facoltativa, per eventi di più giorni)
  - `img`: foto nella cartella `foto/` (es. `foto/olioliva.jpg`); se vuota si usa l'illustrazione
  - `url`: link alla pagina dell'evento o dell'organizzatore
  - `featured: 1` = evento grande in primo piano, `2` e `3` = riquadri accanto
  - Gli eventi già finiti spariscono da soli.
- `TODO` — le schede "Cosa fare" (sostituire `url: "#"` con le pagine dei vostri siti).

## Da completare

- Link ai vostri siti: cercare `ESEMPIO-SITO-ITALIANO` e `EXEMPLE-SITE-FRANCAIS`.
- Iscrizione newsletter: collegare il `<form>` al vostro servizio (Mailchimp, Brevo, ...).
- Gli eventi del N° 1 sono esempi: verificare date e link prima di pubblicare.

## Collegamento dai vostri siti

Aggiungere `?lang=` all'indirizzo per aprire il giornalino già nella lingua giusta:
`it`, `fr`, `en`, `de`, `nl`, `zh` (es. `https://<indirizzo>/index.html?lang=de`).
Senza parametro si usa la lingua del browser del visitatore.

## Foto

Le foto vengono da Wikimedia Commons con licenza libera (CC BY / CC BY-SA / CC0).
Autori e licenze sono elencati in fondo alla pagina ("Crediti foto") e in `foto/CREDITI.md`:
se sostituite una foto, aggiornate anche il credito.
