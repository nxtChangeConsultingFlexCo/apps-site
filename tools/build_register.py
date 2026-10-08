#!/usr/bin/env python3
"""Erzeugt das App-Register für nxtchange.app (Startseite, Impressum, Datenschutz der Website).

Aufruf im Repo-Wurzelordner: python3 -I tools/build_register.py .
Neue App: einen Eintrag in APPS ergänzen und neu erzeugen. Icons liegen unter <ausgabeordner>/assets/.
"""
import html
import pathlib
import sys

OUT = pathlib.Path(sys.argv[1])
STAND = "8. Oktober 2026"

# Reihenfolge: live zuerst, dann im Bau. Status: "live" | "bau"
APPS = [
    {
        "name": "Auszeit",
        "english": "Off Hours",
        "status": "live",
        "status_text": "Im App Store seit 8. Oktober 2026",
        "kurz": "Hält gewählte Apps zu festen Zeiten an und schiebt eine kurze Bedenkzeit dazwischen. Ohne Account, ohne Daten.",
        "plattform": "iPhone, iOS 17 oder neuer",
        "icon": "assets/auszeit-180.png",
        "seite": "https://auszeit.nxtchange.app/",
        "seite_text": "auszeit.nxtchange.app",
        "store": "https://apps.apple.com/at/app/id6817406940",
    },
    {
        "name": "Mappe",
        "english": None,
        "status": "bau",
        "status_text": "In Entwicklung",
        "kurz": "Der Notfallordner der Familie: Was im Ernstfall gebraucht wird, an einem Ort und ohne Suchen.",
        "plattform": "iPhone",
        "icon": None,
        "seite": None,
        "seite_text": "mappe.family (in Vorbereitung)",
        "store": None,
    },
]

CSS = """
/* Register: dunkle Grundfläche mit Goldakzent wie die App-Seiten, eine Spalte, Karten je App */
:root{--bg:#121214;--card:#1b1b1e;--fg:#f1efe9;--muted:#a9a7a0;--gold:#c8b48a;--line:#2b2b2f;--live:#8fc9a0;--maxw:760px;color-scheme:dark}
@media (prefers-color-scheme:light){:root:not([data-theme="dark"]){--bg:#f6f4ee;--card:#fff;--fg:#1a1a1c;--muted:#5d5b55;--gold:#8a7445;--line:#e2dfd6;--live:#2f7a4a;color-scheme:light}}
:root[data-theme="light"]{--bg:#f6f4ee;--card:#fff;--fg:#1a1a1c;--muted:#5d5b55;--gold:#8a7445;--line:#e2dfd6;--live:#2f7a4a;color-scheme:light}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
a{color:var(--gold)}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 16px}
header.top{display:flex;align-items:center;justify-content:space-between;padding:20px 0}
header.top .brand{color:var(--fg);text-decoration:none;font-weight:600;letter-spacing:.01em}
header.top nav a{color:var(--muted);text-decoration:none;margin-left:18px;font-size:15px}
header.top nav a:hover{color:var(--fg)}
.kicker{color:var(--gold);letter-spacing:.14em;text-transform:uppercase;font-size:12px;font-weight:600}
h1{font-family:"New York","Iowan Old Style",Georgia,"Times New Roman",serif;font-weight:600;font-size:clamp(32px,6vw,48px);line-height:1.1;margin:10px 0 14px;letter-spacing:-.01em;text-wrap:balance}
h2{font-family:"New York","Iowan Old Style",Georgia,"Times New Roman",serif;font-weight:600;font-size:26px;margin:0 0 12px;letter-spacing:-.01em}
.lead{font-size:19px;color:var(--muted);max-width:620px;margin:0 0 30px}
.apps{display:grid;gap:16px;margin:0;padding:0;list-style:none}
.app{display:grid;grid-template-columns:72px 1fr;gap:18px;padding:20px;background:var(--card);border:1px solid var(--line);border-radius:18px}
.app .icon{width:72px;height:72px;border-radius:16px;display:block}
.app .icon.empty{border:1px dashed var(--line);display:flex;align-items:center;justify-content:center;color:var(--muted);font-size:22px;font-family:Georgia,serif}
.app h2{margin:0 0 4px;font-size:24px}
.app h2 small{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-weight:400;color:var(--muted);font-size:15px;margin-left:8px}
.status{display:inline-block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;font-weight:600;padding:3px 9px;border-radius:999px;border:1px solid var(--line);color:var(--muted);margin-bottom:8px}
.status.live{color:var(--live);border-color:var(--live)}
.app p{margin:0 0 10px;color:var(--fg)}
.meta{color:var(--muted);font-size:15px;display:flex;flex-wrap:wrap;gap:6px 18px}
.meta a{color:var(--gold)}
section.text{padding:30px 0;border-top:1px solid var(--line);margin-top:30px}
section.text p{max-width:620px}
footer{border-top:1px solid var(--line);padding:28px 0 40px;color:var(--muted);font-size:14px;margin-top:30px}
footer .links a{margin-right:18px;color:var(--fg);text-decoration:none}
footer .links a:hover{text-decoration:underline}
footer address{font-style:normal;margin:16px 0 0;line-height:1.5}
footer .note{margin-top:16px}
@media (max-width:480px){.app{grid-template-columns:56px 1fr;gap:14px;padding:16px}.app .icon{width:56px;height:56px;border-radius:13px}}
"""

ADDRESS = """      <address>
        <strong>nxtChange Consulting FlexCo</strong> · Neugasse 9/1 · 8045 Graz, Österreich<br>
        FN 648962g, Landesgericht für ZRS Graz · UID ATU81922038 · <a href="mailto:apps@nxtchange-consulting.com">apps@nxtchange-consulting.com</a>
      </address>"""


def shell(title: str, desc: str, body: str, root: str) -> str:
    e = html.escape
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <meta name="color-scheme" content="dark light">
  <link rel="icon" href="{root}assets/favicon.png" type="image/png">
  <style>{CSS}</style>
</head>
<body>
  <div class="wrap">
    <header class="top">
      <a class="brand" href="{root}">nxtChange Apps</a>
      <nav>
        <a href="{root}#kontakt">Kontakt</a>
        <a href="{root}impressum/">Impressum</a>
      </nav>
    </header>
{body}
    <footer>
      <div class="links">
        <a href="{root}impressum/">Impressum</a>
        <a href="{root}datenschutz/">Datenschutz</a>
        <a href="https://www.nxtchange-consulting.com/">nxtchange-consulting.com</a>
      </div>
{ADDRESS}
      <p class="note">Apple, iPhone und App Store sind Marken der Apple Inc.</p>
    </footer>
  </div>
</body>
</html>
"""


def app_card(a: dict) -> str:
    e = html.escape
    icon = (f'<img class="icon" src="{e(a["icon"])}" alt="" width="72" height="72">' if a["icon"]
            else f'<div class="icon empty" aria-hidden="true">{e(a["name"][0])}</div>')
    english = f' <small>English: {e(a["english"])}</small>' if a["english"] else ""
    meta = [f"<span>{e(a['plattform'])}</span>"]
    if a["store"]:
        meta.append(f'<a href="{e(a["store"])}">Im App Store</a>')
    if a["seite"]:
        meta.append(f'<a href="{e(a["seite"])}">{e(a["seite_text"])}</a>')
    elif a["seite_text"]:
        meta.append(f"<span>{e(a['seite_text'])}</span>")
    return f"""      <li class="app">
        {icon}
        <div>
          <span class="status {a['status']}">{e(a['status_text'])}</span>
          <h2>{e(a['name'])}{english}</h2>
          <p>{e(a['kurz'])}</p>
          <div class="meta">{' '.join(meta)}</div>
        </div>
      </li>"""


index_body = f"""    <div class="kicker">Register</div>
    <h1>Apps von nxtChange Consulting.</h1>
    <p class="lead">Kleine Werkzeuge für den Alltag, entwickelt in Graz. Diese Seite führt alle Apps, auch die, die noch im Bau sind.</p>
    <ul class="apps">
{chr(10).join(app_card(a) for a in APPS)}
    </ul>
    <section class="text" id="kontakt">
      <h2>Kontakt</h2>
      <p>Fragen, Fehler und Wünsche zu allen Apps: <a href="mailto:apps@nxtchange-consulting.com">apps@nxtchange-consulting.com</a>. Wir antworten in der Regel innerhalb weniger Werktage.</p>
      <p>Stand: {STAND}</p>
    </section>
"""

impressum_body = """    <div class="kicker">Impressum</div>
    <h1>Anbieter dieser Website und der Apps</h1>
    <section class="text" style="border-top:0;padding-top:0;margin-top:0">
      <p>
        nxtChange Consulting FlexCo<br>
        Neugasse 9/1<br>
        8045 Graz, Österreich
      </p>
      <p>
        Firmenbuchnummer: FN 648962g<br>
        Firmenbuchgericht: Landesgericht für ZRS Graz<br>
        UID: ATU81922038
      </p>
      <p>
        E-Mail: <a href="mailto:apps@nxtchange-consulting.com">apps@nxtchange-consulting.com</a><br>
        Ansprechpartner: Karl Maier
      </p>
      <p>Diese Website informiert über die Apps der nxtChange Consulting FlexCo. Die Rechtstexte der einzelnen Apps (Nutzungsbedingungen, Datenschutz, Support) stehen auf der Seite der jeweiligen App.</p>
    </section>
"""

datenschutz_body = """    <div class="kicker">Datenschutz</div>
    <h1>Datenschutz auf dieser Website</h1>
    <section class="text" style="border-top:0;padding-top:0;margin-top:0">
      <p>Diese Website liegt bei GitHub Pages, einem Dienst der GitHub, Inc. (USA). Beim Aufruf verarbeitet GitHub technisch nötige Daten wie deine IP-Adresse, um die Seite auszuliefern. Wir selbst setzen hier keine Cookies, keine Analyse und keine Skripte von Dritten ein. Für die Verarbeitung durch GitHub gilt dessen Datenschutzerklärung: <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">docs.github.com/site-policy/privacy-policies/github-general-privacy-statement</a></p>
      <p>Rechtsgrundlage ist unser berechtigtes Interesse, diese Seiten abrufbar zu halten (Art. 6 Abs. 1 lit. f DSGVO).</p>
      <p>Schreibst du uns eine E-Mail, verarbeiten wir deine Angaben nur, um die Anfrage zu beantworten. Verantwortlich ist die nxtChange Consulting FlexCo, Neugasse 9/1, 8045 Graz, apps@nxtchange-consulting.com. Du hast das Recht auf Auskunft, Berichtigung, Löschung und Beschwerde bei der österreichischen Datenschutzbehörde.</p>
      <p>Was die einzelnen Apps verarbeiten, steht in der Datenschutzerklärung der jeweiligen App.</p>
      <p>Stand: """ + STAND + """</p>
    </section>
"""

pages = [
    ("index.html", "nxtChange Apps", "Register der Apps von nxtChange Consulting FlexCo, Graz: Auszeit und weitere.", index_body, "./"),
    ("impressum/index.html", "Impressum", "Anbieterangaben der nxtChange Consulting FlexCo.", impressum_body, "../"),
    ("datenschutz/index.html", "Datenschutz", "Datenschutz auf nxtchange.app.", datenschutz_body, "../"),
]
for rel, title, desc, body, root in pages:
    body = body.replace('src="assets/', f'src="{root}assets/')
    target = OUT / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(shell(title, desc, body, root), encoding="utf-8")
    print(f"{target} ({target.stat().st_size // 1024} KB)")
