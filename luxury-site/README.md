# Riviera Rent Luxury — sito separato

Sito Luxury indipendente da Riviera Rent France, con dentro la rivista **Live the Riviera**.

- `index.html` — sito in inglese: collezione (Villa Gabriella, La Dragonnière, Kristal Palace, Elidia Palace), concierge, proprietari, rivista, contatti.
- `fr/index.html` — versione francese.
- `magazine/index.html` — la rivista Live the Riviera (EN / FR / IT, `?lang=`).
- `assets/` — stile, logo e script (contatti e prenotazione in `assets/js/config.js`, residenze in `assets/js/properties.js`).

Le residenze sono state tolte: il sito presenta solo concierge, proprietari e il magazine "Live the Riviera".
La cartella `luxury/` del repository resta la sorgente della rivista: dopo ogni modifica, copiarla in `luxury-site/magazine/`.
