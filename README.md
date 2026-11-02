# apps-site

Register der Apps von nxtChange Consulting FlexCo, erreichbar unter https://nxtchange.app (GitHub Pages, Branch
`main`, Wurzelordner, statisches HTML ohne Jekyll).

- `index.html` Startseite mit allen Apps, `impressum/`, `datenschutz/` (Datenschutz dieser Website)
- `robots.txt` (alles erlaubt, KI-Crawler ausdrücklich genannt), `sitemap.xml` (die drei Seiten mit `STAND_ISO` als
  lastmod) und `llms.txt` (Kurzfassung für Sprachmodelle, aus `APPS` gespeist) im Wurzelordner
- `tools/build_register.py` erzeugt die drei Seiten und diese drei Dateien; die App-Liste steht im Skript (`APPS`).
  Neue App: Eintrag ergänzen, `python3 -I tools/build_register.py .` ausführen, committen.
  Je App steht dort auch der Langtext für die Startseite (`lang`, Liste von Absätzen; keine Eurobeträge, bei Mappe keine
  Gesundheitsversprechen).
- `assets/` Icons (180 px je App, Favicon 96 px, Apple-Touch-Icon 180 px), dazu `favicon.ico` im Wurzelordner. Favicon und
  Touch-Icon zeigen den nxt-Schriftzug dunkel eingraviert in poliertes Gold, damit sich das Register vom schwarz-weißen
  Icon der Firmen-Website abhebt. Sie entstehen mit `swift tools/icons.swift` aus `assets/nxt.png`.
- `CNAME` bindet die Domain; die DNS-Einträge liegen bei Hostinger.

Die Seiten der einzelnen Apps haben eigene Repos, zum Beispiel `auszeit-legal` für auszeit.nxtchange.app.

Jede Seite hat Canonical, Open Graph und JSON-LD (Startseite: Organisation, Website und die Apps als Liste, Unterseiten:
WebPage). [[KARL BESTÄTIGEN]] Vorschaubild 1200×630 für nxtchange.app fehlt; vorerst das Touch-Icon (`OG_IMAGE` im Skript).
