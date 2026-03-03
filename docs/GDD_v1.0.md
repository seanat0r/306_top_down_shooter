# Game Design Document TD-Shooter

## 1. Spielüberblick
- Genre:
- Ziel des Spiels:
- Zielplattform: (Python EXE, OS)
- Zielgruppe:

## 2. Gameplay und Regeln
- Spielfigur: Bewegung, Leben, Geschwindigkeit
- Gegner: Typen, Verhalten (z.B. verfolgen, schiessen)
- Steuerung: Tasten für Bewegung, Schiessen, Pause
- Punkte/Score: Wie erhält man Punkte? Highscore?
- Spielende: Wann ist verloren / gewonnen? Restart?

## 3. Level und Content
- Anzahl Level (für MVP):
- Levelaufbau: Grösse, Layout grob beschrieben
- Schwierigkeit: Wie steigt sie an?

## 4. Benutzeroberfläche (UI/UX)
- Hauptscreen: Was wird angezeigt? (Spiel, HP, Score)
- Start-/Endbildschirm: Welche Infos, welche Buttons?
- Einfacher Mockup-Link oder kurze Beschreibung.

## 5. Technisches Konzept / Architektur
- Technologie: Python-Version, Libraries (z.B. pygame)
- Hauptmodule/Klassen:
  - Game Loop
  - Player
  - Enemy
  - Bullet/Projectile
  - Level/Map
- Datenfluss kurz: Wer ruft wen auf? Wo liegen Ressourcen (Sprites, Sounds)?

## 6. Nicht-funktionale Anforderungen
- Performance: Ziel FPS, maximale Gegneranzahl
- Bedienbarkeit: Vollscreen/Fenster, Steuerung konfigurierbar (ja/nein)
- Portabilität: Auf welchen Schulrechnern muss es laufen?

## 7. Abnahmekriterien (Aus Sicht BA/AG)
- Liste von 5–10 „Das Spiel gilt als fertig, wenn …“-Punkten
  - z.B. „Der Spieler kann sich in vier Richtungen bewegen.“
  - „Mindestens ein Level ist komplett durchspielbar.“
  - „Score wird angezeigt und nach Game Over bleibt sichtbar.“