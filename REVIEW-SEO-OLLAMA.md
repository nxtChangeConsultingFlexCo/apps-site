<!-- Zweitmeinung aus Ollama (Alias review = kimi-k3) über /work/bin/llm, 02.11.2026, auf Basis des Diffs main..seo/2026-11 (Commits 3ecb698, de15f22, 6d40c98).
     Nur gelesen, nichts geändert. Vom Orchestrator (Claude) gegengeprüft:
     Frage 2: ja, nxt-site (Branch seo/2026-11, Commit 4bad81c) trägt die Organization mit derselben @id https://nxtchange-consulting.com/#unternehmen; auf dem Live-Stand (main) ist sie noch nicht enthalten.
     Frage 3: ja, auszeit.nxtchange.app/llms.txt und mappe.family/llms.txt antworten mit 200 (02.11.2026).
     Frage 4: ja, der Datenschutztext enthält „keine Cookies, keine Analyse und keine Skripte von Dritten“.
     Fragen 1 und 5 sowie alle übrigen Punkte sind Einschätzungen des Modells bzw. liegen bei Karl ([[KARL BESTÄTIGEN]] in STATUS.md). -->
# Zweitmeinung (Ollama) zu Branch seo/2026-11 – apps-site (nxtchange.app)

## Kurzurteil
Die Pakete A1–A3 sind sauber und buildseitig konsistent umgesetzt: Canonical, Open Graph und JSON-LD sind formal korrekt, robots.txt und sitemap.xml wohlgeformt, die redaktionellen Leitplanken (keine Preise, keine Gesundheitsversprechen zu Mappe) sind im Diff nachweisbar eingehalten. Blocker gibt es nicht. Freigabe-Empfehlung: ja, mit Auflagen – das OG-Bild ist ein 180×180-Provisorium unter den üblichen Mindestmaßen, und die `[[KARL BESTÄTIGEN]]`-Marker sollten vor dem Merge aufgelöst werden. Zwei Aussagen (Datenschutz-Description, Fakten der Langtexte) sind aus dem Diff nicht gegen die Quellen prüfbar und brauchen eine Bestätigung.

## Befunde

| Nr | Schwere | Datei/Stelle | Befund | Empfehlung |
|---|---|---|---|---|
| 1 | mittel | `tools/build_register.py` (`OG_IMAGE`), heads aller drei Seiten | `og:image` ist das 180×180-Touch-Icon (`og:image:width/height` = 180). Gängige Plattformen (Facebook/Meta, LinkedIn) erwarten mindestens 200×200 px, empfohlen 1200×630 – die Linkvorschau beim Teilen ist damit unsicher. Autor hat dies selbst mit `[[KARL BESTÄTIGEN]]` markiert. | 1200×630-Bild erstellen und `OG_IMAGE` umstellen; bis dahin als dokumentiertes Provisorium führen, nicht als „fertig“. |
| 2 | niedrig | `tools/build_register.py` (`sitemap_xml()`), `sitemap.xml` | `lastmod` = globales `STAND_ISO` (2026-11-02) für alle drei Seiten. Der Datenschutzinhalt ist laut Kommentar zu `STAND_DATENSCHUTZ` seit 14.10.2026 unverändert; `lastmod` suggeriert eine Änderung am 2.11. Google wertet pauschale lastmod-Angaben als verrauschtes Signal. | lastmod je Seite pflegen (z. B. eigenes Datum für datenschutz/) oder bewusst so lassen und dokumentieren. |
| 3 | niedrig | `index.html` JSON-LD, `ItemList` | `SoftwareApplication`-Einträge ohne `offers` und ohne `aggregateRating`; Google qualifiziert Software-App-Rich-Results nur mit mindestens einem der beiden. Folge der Vorgabe „keine Preise“, kein Markup-Fehler – aber keine Rich-Result-Eignung. | So lassen. Nur ergänzen, falls Preisangaben später freigegeben werden. |
| 4 | niedrig | `index.html` App-Karten, `app_card()` | `alt="App-Icon von Auszeit"` usw. steht unmittelbar vor dem `<h2>` mit demselben App-Namen; Screenreader lesen den Namen doppelt. Bei rein dekorativen Icons wäre `alt=""` die WCAG-übliche Wahl. A2-Auftrag verlangte jedoch Alt-Texte. | Bewusste Entscheidung dokumentieren oder bei Priorität Barrierefreiheit auf `alt=""` zurückstellen. |
| 5 | niedrig | `README.md`, `tools/build_register.py` (Kommentar) | Unaufgelöste Marker `[[KARL BESTÄTIGEN]]` im Branch (nicht im generierten HTML). | Vor Merge bestätigen bzw. entfernen. |
| 6 | niedrig | `datenschutz/index.html`, Description/JSON-LD | Die neue Description behauptet „keine Cookies, keine Analyse, keine Skripte von Dritten“. Der Body der Datenschutzseite ist nicht Teil des Diff; die Deckung mit dem tatsächlichen Text ist nicht ableitbar. | Inhalt der Datenschutzseite gegen die Description verifizieren (siehe Fragen). |

## Geprüft und in Ordnung

- Canonical je Seite, konsistent zu `og:url` und Sitemap-`<loc>`, überall mit Trailing Slash (`/`, `/impressum/`, `/datenschutz/`).
- Open Graph vollständig auf allen drei Seiten: type, site_name, title, description, url, locale `de_AT`, image inkl. width/height/alt.
- JSON-LD formal korrekt: `@graph` mit Organization (Adresse, E-Mail, founder), WebSite, ItemList mit `ListItem position` 1–3; Unterseiten WebPage mit `isPartOf`-Verweis auf `#website`. `json.dumps` mit Escape `</` → `<\/` gegen Script-Breaking; Syntax per Konstruktion valide.
- `applicationCategory`-Werte (`UtilitiesApplication`, `FinanceApplication`, `HealthApplication`) sind die üblichen schema-/Google-Werte; Trennung `os` (JSON-LD) vs. `plattform` (Anzeige) sauber gelöst.
- robots.txt syntaktisch korrekt: mehrere `User-agent`-Zeilen mit einem gemeinsamen `Allow: /` bilden nach RFC 9309 eine Gruppe; Sitemap-Zeile absolut und korrekt.
- sitemap.xml wohlgeformt, korrekter Namespace, ISO-Datumformat.
- llms.txt folgt der Konvention (H1, Blockquote, H2-Sektionen); Konsistenz zur Startseite durch gemeinsame `AUSNAHMEN`-Konstante gesichert; `{wer}`-Platzhalter in beiden Varianten grammatikalisch korrekt aufgelöst.
- Textlänge A3 erfüllt: die neuen Abschnitte allein liegen deutlich über 600 Wörtern (im Diff zählbar); die gemeldeten 1000 inkl. Bestand sind plausibel.
- Redaktionelle Regeln eingehalten: keine Eurobeträge im gesamten Diff; Mappe-Sektion endet mit „Alles Weitere:“ (ohne Preisverweis, anders als Auszeit/Stapel), Disclaimer „kein Medizinprodukt“ statt Heilsversprechen; Preisregel kostenlos/Mappe Plus entspricht der Vorgabe.
- Meta-Descriptions: Startseite ≈152 Zeichen (im Diff zählbar, < 160); Unterseiten laut Angabe 129/143 Zeichen, Strings plausibel.
- Titles sprechend und kurz (~25 bzw. ~50 Zeichen).
- hreflang entfällt zu Recht: Site ist einsprachig (`lang="de"`, `inLanguage: de`, `og:locale de_AT` konsistent).
- Stand aktualisiert (25.10. → 2.11.2026), `STAND` und `STAND_ISO` derzeit deckungsgleich.
- Generierte HTML-Dateien stimmen mit dem Skript überein (Stichproben: Meta-Blöcke, JSON-LD, Alt-Texte, Abschnitte).

## Restrisiken vor dem Merge

- OG-Bild-Provisorium: Teilen auf Plattformen mit Mindestgröße 200×200 ggf. ohne Vorschaubild, solange `OG_IMAGE` nicht ersetzt ist.
- `STAND`/`STAND_ISO` werden manuell doppelt gepflegt; Divergenzrisiko bei künftigen Edits.
- `INDEX_DESC` und der Index-Title werden aus der App-Liste gebaut – wachsen mit jeder neuen App; Längenlimit (>160 bzw. ~60–70 Zeichen) bei 4+ Apps beobachten.
- lastmod-Pauschalierung: Änderungen nur am Datenschutz-Text aktualisieren das Sitemap-lastmod nicht automatisch.
- Externe Verweise nicht prüfbar: `auszeit.nxtchange.app/llms.txt`, `mappe.family/llms.txt`, `portal.mappe.family` (als Text in der Mappe-Sektion) – Existenz aus dem Diff nicht ableitbar.
- Inhaltliche Fakten der Langtexte (z. B. „37 Länder App Store / 36 Google Play“, „bis zu zehn Angehörige“, Rechte-Modell Notfall/Alltag/Vertraulich) sind im Diff formuliert, aber ihre Beleglage auf den Quellseiten nicht prüfbar.

## Fragen an den Autor

1. Wird das 1200×630-OG-Bild vor dem Merge geliefert, oder mergen wir bewusst mit dem Provisorium? Falls letzteres: wo wird die Nachlieferung getrackt?
2. Existiert auf nxtchange-consulting.com ein JSON-LD mit derselben `@id` (`https://nxtchange-consulting.com/#unternehmen`), damit die Entity-Verknüpfung beidseitig belegt ist?
3. Sind die in der eigenen `llms.txt` verlinkten Dateien `auszeit.nxtchange.app/llms.txt` und `mappe.family/llms.txt` tatsächlich live?
4. Deckt die neue Datenschutz-Description („keine Cookies, keine Analyse, keine Skripte von Dritten“) den bestehenden Datenschutztext ab? Der Body war nicht im Diff.
5. Sind die neuen Langtext-Fakten (Länderzahlen Auszeit, Obergrenzen Mappe Plus, Rechte-Modell) von Karl fachlich bestätigt, oder steht die Bestätigung wie beim OG-Bild noch aus?
