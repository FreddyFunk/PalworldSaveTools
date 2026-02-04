<div align="center">

![PalworldSaveTools Logo](https://github.com/deafdudecomputers/PalworldSaveTools/blob/main/resources/PalworldSaveTools_Blue.png)

# PalworldSaveTools

**Ein umfassendes Toolkit zur Bearbeitung gespeicherter Dateien für Palworld**

[![Downloads](https://img.shields.io/github/downloads/deafdudecomputers/PalworldSaveTools/total)](https://github.com/deafdudecomputers/PalworldTools/releases/latest)
[![Lizenz](https://img.shields.io/github/license/deafdudecomputers/PalworldSaveTools)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join_for_support-blue)](https://discord.gg/sYcZwcT4cT)
[![NexusMods](https://img.shields.io/badge/NexusMods-Download-orange)](https://www.nexusmods.com/palworld/mods/3190)

[English](https://github.com/deafdudecomputers/PalworldSaveTools/blob/main/README.md) | [zh-CN](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.zh_CN.md) | [de-DE](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.de_DE.md) | [es-ES](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.es_ES.md) | [fr-FR](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.fr_FR.md) | [ru-RU](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.ru_RU.md) | [ja-JP](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.ja_JP.md) | [ko-KR](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.ko_KR.md)

---

### **Download the standalone version from [GitHub Veröffentlichungen](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest)**

---

</div>

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Tools Overview](#tools-overview)
- [Guides](#guides)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Kernfunktionalität

| Besonderheit | Beschreibung |
| --------- | ------------- |
| **Schnelles Speichern-Parsen** | Einer der schnellsten verfügbaren Lesegeräte für gespeicherte Dateien |
| **Spielerverwaltung** | Anzeigen, Bearbeiten, Umbenennen, Levelwechsel, Freischalten von Technologien und Verwalten von Spielern |
| **Gildenverwaltung** | Erstellen Sie Spieler, benennen Sie sie um, verschieben Sie sie, schalten Sie Laborforschung frei und verwalten Sie Gilden |
| **Kumpel-Editor** | Vollständiger Editor für Statistiken, Fertigkeiten, IVs, Rang, Seelen, Geschlecht, Boss/Glücksbringer-Umschaltung |
| **Basislager-Werkzeuge** | Exportieren, importieren, klonen, Radius anpassen und Basen verwalten |
| **Kartenbetrachter** | Interaktive Basis- und Spielerkarte mit Koordinaten und Details |
| **Charakterübertragung** | Charaktere zwischen verschiedenen Welten/Servern übertragen (Cross-Save) |
| **Konvertierung speichern** | Konvertieren Sie zwischen den Formaten Steam und GamePass |
| **Welteinstellungen** | Bearbeiten Sie die Einstellungen für WorldOption und LevelMeta |
| **Zeitstempel-Tools** | Korrigieren Sie negative Zeitstempel und setzen Sie die Spielerzeiten zurück |

### All-in-One-Tools

Die Suite **All-in-One Tools** bietet umfassende Speicherverwaltung:

- **Löschwerkzeuge**
  - Löschen Sie Players, Basen oder Gilden
  - Löschen Sie inaktive Spieler basierend auf Zeitschwellen
  - Entfernen Sie doppelte Spieler und leere Gilden
  - Löschen Sie nicht referenzierte/verwaiste Daten

- **Bereinigungstools**
  - Entfernen Sie ungültige/modifizierte Elemente
  - Entfernen Sie ungültige Kumpels und Passive
  - Illegale Freunde reparieren (Grenze auf legale Maximalwerte)
  - Entfernen Sie ungültige Strukturen
  - Luftabwehrtürme zurücksetzen
  - Schalte private Truhen frei

- **Gildenwerkzeuge**
  - Alle Gilden neu aufbauen
  - Verschiebe Spieler zwischen Gilden
  - Ernenne den Spieler zum Gildenführer
  - Gilden umbenennen
  - Maximales Gildenlevel
  - Schalten Sie alle Laborforschungen frei

- **Player-Tools**
  - Bearbeiten Sie die Statistiken und Fähigkeiten von Spielerfreunden
  - Schalten Sie alle Technologien frei
  - Schalte den Sichtkäfig frei
  - Spieler im Level auf-/absteigen
  - Spieler umbenennen

- **Speichern Sie Dienstprogramme**
  - Missionen zurücksetzen
  - Dungeons zurücksetzen
  - Zeitstempel korrigieren
  - Reduzieren Sie überfüllte Lagerbestände
  - Generieren Sie PalDefender-Befehle

### Zusätzliche Tools

| Werkzeug | Beschreibung |
| ------ | ------------- |
| **Spielerfreunde bearbeiten** | Vollständiger Kumpel-Editor mit Statistiken, Fähigkeiten, IVs, Talenten, Seelen, Rang und Geschlecht |
| **SteamID-Konverter** | Konvertieren Sie Steam-IDs in Palworld UIDs |
| **Host-Speicherung beheben** | Tauschen Sie UIDs zwischen zwei Spielern aus (z. B. für den Host-Tausch) |
| **Spieler tauschen UIDs** | Tausche UIDs zwischen zwei Spielern |
| **Schlitzinjektor** | Erhöhen Sie die Palbox-Slots pro Spieler |
| **Karte wiederherstellen** | Wende den freigeschalteten Kartenfortschritt auf alle Welten/Server an |
| **Welt umbenennen** | Weltnamen in LevelMeta ändern |
| **WorldOption Herausgeber** | Bearbeiten Sie die Welteinstellungen und -konfiguration |
| **LevelMeta Herausgeber** | Weltmetadaten bearbeiten (Name, Host, Level) |
| **Koordinatenkonverter** | Konvertieren Sie Koordinaten im Spiel |

---

## Installation

### Voraussetzungen

**Für Standalone (Windows):**
- Windows 10/11
- [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version) (2015–2022)

**Zur Ausführung aus dem Quellcode (Linux oder Entwicklung):**
- Python 3.10 oder höher
- pip (Python Paketmanager)

### Eigenständig (Windows – empfohlen)

1. Laden Sie die neueste Version von [GitHub Releases](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest) herunter.
2. Extrahieren Sie die ZIP-Datei
3. Führen Sie „PalworldSaveTools.exe“ aus

### Aus der Quelle (Linux oder für die Entwicklung)

```bash
git clone https://github.com/deafdudecomputers/PalworldSaveTools.git
cd PalworldSaveTools
pip install -r requirements.txt
python start.py
```

---

## Quick Start

1. **Laden Sie Ihren Speicherstand**
   - Klicken Sie auf **Datei → Laden und Speichern**
   - Navigieren Sie zu Ihrem Palworld-Speicherordner
   - Wählen Sie „Level.sav“.

2. **Erkunden Sie Ihre Daten**
   - Verwenden Sie die Registerkarten, um Players, Gilden, Stützpunkte oder die Karte anzuzeigen
   - Suchen und filtern Sie, um bestimmte Einträge zu finden

3. **Änderungen vornehmen**
   - Wählen Sie Elemente zum Bearbeiten, Löschen oder Ändern aus
   - Verwenden Sie Kontextmenüs für zusätzliche Optionen

4. **Speichern Sie Ihre Änderungen**
   - Klicken Sie auf **Datei → Änderungen speichern**.
   - Backups werden automatisch erstellt

---

## Tools-Übersicht

### All-in-One-Tools (AIO)

Die Hauptoberfläche für eine umfassende Speicherverwaltung mit drei Registerkarten:

**Players Tab** – Alle Spieler auf dem Server anzeigen und verwalten
- Bearbeiten Sie Spielernamen, Level und Freundeszahlen
- Löschen Sie inaktive Spieler
- Spielergilden und letzte Onlinezeit anzeigen

**Registerkarte „Gilden“** – Gilden und ihre Basen verwalten
- Gilden umbenennen, Anführer wechseln
- Zeigen Sie Basisstandorte und -ebenen an
- Leere oder inaktive Gilden löschen

**Registerkarte „Stützpunkte“** – Alle Basislager anzeigen
- Basis-Blaupausen exportieren/importieren
- Klonen Sie Basen für andere Gilden
- Basisradius anpassen

### Kartenbetrachter

Interaktive Visualisierung Ihrer Welt:
- Alle Basisstandorte und Spielerpositionen anzeigen
- Filtern Sie nach Gilde oder Spielername
- Klicken Sie auf die Markierungen, um detaillierte Informationen zu erhalten
- Generieren Sie „killnearestbase“-Befehle für PalDefender

### Charakterübertragung

Charaktere zwischen verschiedenen Welten/Servern übertragen (Cross-Save):
- Übertragen Sie einzelne oder alle Spieler
- Behält Charaktere, Freunde, Inventar und Technologie bei
- Nützlich für die Migration zwischen Genossenschaft und dedicated servers

### Host-Speicherung beheben

Tausche UIDs zwischen zwei Spielern:
- Übertragen Sie den Fortschritt von einem Spieler auf einen anderen
- Unverzichtbar für host/co-op-zu-Server-Übertragungen
- Nützlich für den Austausch der Host-Rolle zwischen Spielern
- Nützlich für Plattformwechsel (Xbox ↔ Steam)
- Behebt Probleme bei der Zuordnung von Host/Server UID
- **Notiz:** Affected player must have a character created on the target save first

---

## Anleitungen

### Dateispeicherorte speichern

**Gastgeber/Kooperative:**
```
%localappdata%\Pal\Saved\SaveGames\YOURID\RANDOMID\
```

**Dedizierter Server:**
```
steamapps\common\Palworld\Pal\Saved\SaveGames\0\RANDOMSERVERID\
```

### Kartenfreischaltung

<Details>
<summary>Klicken Sie hier, um die Anweisungen zum Entsperren der Karte zu erweitern</summary>

1. Kopieren Sie „LocalData.sav“ aus „src\resources\“.
2. Suchen Sie Ihren Server-/Weltspeicherordner
3. Ersetzen Sie die vorhandene Datei „LocalData.sav“ durch die kopierte Datei
4. Starten Sie das Spiel mit einer vollständig freigeschalteten Karte

> **Hinweis:** Verwenden Sie die Option **Extras → Karte wiederherstellen** in PST, um die freigeschaltete Karte mit automatischen Backups auf ALLE Ihre Welten/Server gleichzeitig anzuwenden.

</details>

### Host → Serverübertragung

<Details>
<summary>Klicken Sie hier, um die Host-zu-Server-Übertragungsanleitung zu erweitern</summary>

1. Kopieren Sie die Ordner „Level.sav“ und „Players“ vom Hostspeicher
2. In den Speicherordner dedicated server einfügen
3. Server starten, neuen Charakter erstellen
4. Warten Sie auf die automatische Speicherung und schließen Sie dann
5. Verwenden Sie **Fix Host Save**, um GUIDs zu migrieren
6. Kopieren Sie die Dateien zurück und starten Sie sie

**Fix Host Save verwenden:**
- Wählen Sie „Level.sav“ aus Ihrem temporären Ordner aus
- Wähle den **alten Charakter** (aus dem Originalspeicher)
- Wählen Sie den **neuen Charakter** (den Sie gerade erstellt haben)
- Klicken Sie auf **Migrieren**

</details>

### Host Swap (Host wechseln)

<Details>
<summary>Klicken Sie hier, um die Host-Swap-Anleitung zu erweitern</summary>

**Hintergrund:**
- Der Host verwendet immer „0001.sav“ – dasselbe UID für jeden Host
- Jeder Client verwendet einen eindeutigen regulären UID-Speicher (z. B. „123xxx.sav“, „987xxx.sav“).

**Voraussetzungen:**
Für beide Spieler (alter Host und neuer Host) müssen ihre regulären Spielstände generiert werden. Dies geschieht, indem man sich der Welt des Gastgebers anschließt und einen neuen Charakter erstellt.

**Schritte:**

1. **Stellen Sie sicher, dass regelmäßige Speicherungen vorhanden sind**
   - Spieler A (alter Host) sollte einen regulären Speicherstand haben (z. B. „123xxx.sav“)
   - Spieler B (neuer Host) sollte einen regulären Speicherstand haben (z. B. „987xxx.sav“)

2. **Host-Speicherung des alten Hosts gegen reguläre Speicherung austauschen**
   - Verwenden Sie PalworldSaveTools **Fix Host Save**, um Folgendes auszutauschen:
   - „0001.sav“ des alten Hosts → „123xxx.sav“.
   - (Dadurch wird der Fortschritt des alten Hosts vom Host-Slot auf den regulären Spieler-Slot verschoben.)

3. **Tauschen Sie den regulären Save des neuen Gastgebers gegen den Host Save um**
   - Verwenden Sie PalworldSaveTools **Fix Host Save**, um Folgendes auszutauschen:
   - Neuer Host: „987xxx.sav“ → „0001.sav“.
   - (Dadurch wird der Fortschritt des neuen Hosts in den Host-Slot verschoben.)

**Ergebnis:**
- Spieler B ist jetzt der Gastgeber mit seinem eigenen Charakter und seinen eigenen Freunden in „0001.sav“.
- Spieler A wird mit seinem ursprünglichen Fortschritt in „123xxx.sav“ zum Client

</details>

### Basis-Export/Import

<Details>
<summary>Klicken Sie hier, um die Basis-Export-/Importanleitung zu erweitern</summary>

**Eine Basis exportieren:**
1. Laden Sie Ihren Speicherstand in PST
2. Gehen Sie zur Registerkarte „Basen“.
3. Klicken Sie mit der rechten Maustaste auf eine Basis → Basis exportieren
4. Als „.json“-Datei speichern

**Eine Basis importieren:**
1. Gehen Sie zur Registerkarte „Basen“ oder zum Base Map Viewer
2. Klicken Sie mit der rechten Maustaste auf die Gilde, in die Sie die Basis importieren möchten
3. Wählen Sie Basis importieren
4. Wählen Sie Ihre exportierte „.json“-Datei aus

**Eine Basis klonen:**
1. Klicken Sie mit der rechten Maustaste auf eine Basis → Basis klonen
2. Zielgilde auswählen
3. Die Basis wird mit versetzter Positionierung geklont

**Anpassen des Basisradius:**
1. Klicken Sie mit der rechten Maustaste auf eine Basis → Radius anpassen
2. Neuen Radius eingeben (50 % - 1000 %)
3. Speichern und laden Sie den Speicherstand im Spiel, damit Strukturen neu zugewiesen werden können

</details>

---

## Troubleshooting

### „VCRUNTIME140.dll wurde nicht gefunden“

**Solution:** Install [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version)

### `struct.error` when parsing save

**Ursache:** Veraltetes Speicherdateiformat

**Lösung:**
1. Laden Sie den Speicherstand im Spiel (Solo-, Coop- oder Dedicated-Server-Modus).
2. Dadurch wird eine automatische Strukturaktualisierung ausgelöst
3. Stellen Sie sicher, dass der Speicherstand mit oder nach dem neuesten Spiel-Patch aktualisiert wurde

### GamePass Konverter funktioniert nicht

**Lösung:**
1. Schließen Sie die GamePass-Version von Palworld
2. Warten Sie ein paar Minuten
3. Führen Sie den Konverter Steam → GamePass aus
4. Starten Sie zur Überprüfung Palworld auf GamePass

---

## Aufbau aus der Quelle

```bash
# Clone the repository
git clone https://github.com/deafdudecomputers/PalworldSaveTools.git

# Install dependencies
pip install -r requirements.txt

# Run the application
python start.py
```

Verwenden Sie zum Erstellen der eigenständigen ausführbaren Datei das Build-Skript:
```bash
python scripts/build.py
```

---

## Contributing

Beiträge sind willkommen! Bitte senden Sie gerne einen Pull Request.

1. Forken Sie das Repository
2. Erstellen Sie Ihren Feature-Zweig („git checkout -b feature/AmazingFeature“)
3. Übernehmen Sie Ihre Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Zum Zweig pushen („git push origin feature/AmazingFeature“)
5. Öffnen Sie eine Pull-Anfrage

---

## Haftungsausschluss

**Die Verwendung dieses Tools erfolgt auf eigene Gefahr. Sichern Sie immer Ihre Sicherungsdateien, bevor Sie Änderungen vornehmen.**

Die Entwickler sind nicht verantwortlich für den Verlust gespeicherter Daten oder Probleme, die durch die Verwendung dieses Tools entstehen können.

---

## Unterstützung

- **Discord:** [Join us for support, base builds, and more!](https://discord.gg/sYcZwcT4cT)
- **GitHub Probleme:** [Report a bug](https://github.com/deafdudecomputers/PalworldSaveTools/issues)
- **Dokumentation:** [Wiki](https://github.com/deafdudecomputers/PalworldSaveTools/wiki) *(Currently in development)*

---

## Lizenz

Dieses Projekt ist unter der Lizenz MIT License lizenziert – Einzelheiten finden Sie in der Datei [LICENSE](LICENSE).

---

## Danksagungen

- **Palworld** developed by Pocketpair, Inc.
- Vielen Dank an alle Mitwirkenden und Community-Mitglieder, die zur Verbesserung dieses Tools beigetragen haben

---

<div align="center">

**Erstellt mit ❤️ für die Palworld-Community**

⬆ Zurück nach oben

</div>
