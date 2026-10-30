# La Riviera — il giornalino degli eventi

Giornalino web bilingue (IT/FR) con gli eventi di Genova, Savona, Imperia e Costa Azzurra.
È un unico file: `index.html`. Si apre con qualsiasi browser e si pubblica su qualsiasi hosting.

## Come aggiornarlo per un nuovo numero

Apri `index.html` e cerca **CONTENUTI DEL GIORNALINO**:

- `ISSUE` — numero e mese dell'edizione.
- `EVENTS` — gli eventi. Ogni evento ha:
  - `zone`: `genova` | `savona` | `imperia` | `azur`
  - `cat`: `sagre` | `feste` | `musica` | `mercatini` | `cultura` | `sport`
  - `date`: data di inizio `AAAA-MM-GG` (serve per l'ordine e il badge)
  - `icon`: un'emoji
  - `it` / `fr`: titolo, luogo, quando, una frase breve
  - `url`: link alla pagina dell'evento o dell'organizzatore
  - `featured: true` su un solo evento per metterlo in copertina
- `TODO` — le schede "Cosa fare" (sostituire `url: "#"` con le pagine dei vostri siti).

## Da completare

- Link ai vostri siti: cercare `ESEMPIO-SITO-ITALIANO` e `EXEMPLE-SITE-FRANCAIS`.
- Iscrizione newsletter: collegare il `<form>` al vostro servizio (Mailchimp, Brevo, ...).
- Gli eventi del N° 1 sono esempi: verificare date e link prima di pubblicare.

## Collegamento dai vostri siti

- Sito italiano: `https://<indirizzo>/index.html?lang=it`
- Sito francese: `https://<indirizzo>/index.html?lang=fr`
