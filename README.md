# apps-site

Register der Apps von nxtChange Consulting FlexCo, erreichbar unter https://nxtchange.app (GitHub Pages, Branch
`main`, Wurzelordner, statisches HTML ohne Jekyll).

- `index.html` Startseite mit allen Apps, `impressum/`, `datenschutz/` (Datenschutz dieser Website)
- `tools/build_register.py` erzeugt die drei Seiten; die App-Liste steht im Skript (`APPS`).
  Neue App: Eintrag ergänzen, `python3 -I tools/build_register.py .` ausführen, committen.
- `assets/` Icons (180 px je App, Favicon)
- `CNAME` bindet die Domain; die DNS-Einträge liegen bei Hostinger.

Die Seiten der einzelnen Apps haben eigene Repos, zum Beispiel `auszeit-legal` für auszeit.nxtchange.app.
