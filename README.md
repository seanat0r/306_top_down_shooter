# 306 SCB - Top-Down Shooter

Ein intensiver Survival-Shooter, entwickelt im Rahmen des Moduls 306 mit **Python** und **Pygame-CE**. Überlebe so lange wie möglich gegen feindliche Wellen und maximiere deinen Highscore!

## Installation & Start (Windows)

Das Spiel wird als eigenständige Applikation geliefert und benötigt keine installierte Python-Umgebung.

1. Navigieren Sie/ Laden Sie die den Ordner Herunter in den Ordner `game`.
2. Starten Sie die Datei `TopDownShooter.exe`.
3. **Wichtiger Hinweis:** Da die Datei nicht digital signiert ist, erscheint beim Start möglicherweise der Windows-SmartScreen. Klicken Sie auf **"Weitere Informationen"** -> **"Trotzdem ausführen"**.

---

## Bedienung

| Taste | Aktion |
| :--- | :--- |
| **W, A, S, D** | Bewegung des Charakters |
| **Maus** | Zielen |
| **Linksklick** | Schießen |
| **R** | Nachladen (Manuell oder automatisch) |
| **ESC** | Spiel pausieren / Beenden (im Hauptmenü) |
| **ENTER** | Spiel starten (Menü / Pause) |

---

## Hauptmerkmale (Features)

* **Zwei Level-Umgebungen:** Von einem Einführungslevel bis hin zu komplexen Arealen mit Sackgassen und taktischen Engpässen.
* **Dynamische Skalierung:** Der Schwierigkeitsgrad (Geschwindigkeit und Spawn-Rate) passt sich kontinuierlich dem Score an.
* **Upgrade-Mechanik:** Alle 100 Punkte erfolgt eine automatische Magazinerweiterung (+5 Schuss).
* **Flüssige Steuerung:** Einsatz von "Sliding Collisions" für eine barrierefreie Bewegung an Hindernissen.
* **Benutzerschnittstelle:** Echtzeit-HUD und ein aktives Benachrichtigungssystem für Upgrades und Warnungen.

---

## Technische Umsetzung (EVA-Prinzip)

Die Software-Architektur ist nach dem EVA-Prinzip strukturiert:

1. **Eingabe:** Erfassung von Benutzersignalen über eine zentrale State-Machine.
2. **Verarbeitung:** Vektor-basierte Bewegungslogik und präzise Kollisionsabfragen auf zwei Achsen.
3. **Ausgabe:** Sprite-basiertes Rendering mit stabilen 60 FPS und Overlay-UI.

## Tech-Stack

* **Sprache:** Python 3.12.3
* **Game-Engine:** [pygame-ce](https://pyga.me/) (Community Edition) v2.5.7
* **Testing:** [pytest](https://docs.pytest.org/) für automatisierte Unit-Tests
* **Deployment:** PyInstaller (Erstellung der standalone .exe)

### Projektstruktur & Architektur

Das Projekt folgt einem modularen Ansatz, um die Trennung von Spiellogik, UI und Konfiguration zu gewährleisten:

```text
306_top_down_shooter/
├── src/                # Quellcode (Source)
│   ├── main.py         # Game-Loop & State-Management
│   ├── player.py       # Spieler-Logik (Bewegung, Munition)
│   ├── enemy.py        # KI-Verhalten (Vektor-Tracking)
│   ├── projectile.py   # Projektil-Physik
│   ├── level_manager.py# Szenenwechsel & Hindernisse
│   ├── ui_manager.py   # HUD & Menü-Anzeigen
│   └── config.py       # Zentrale Spiel-Konstanten
├── tests/              # Automatisierte Unit-Tests
└── game/              # Fertige Ordner zum downlaoden
```

---

## Projektteam

Entwickelt im Rahmen der Informatikausbildung (Modul 306).
**Entwickler:** Stefanie Gerber, Benjamin Phengrasamy, Sujanthan Suntheralingam, Christophe Grädel
