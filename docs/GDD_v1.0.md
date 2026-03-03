# Game Design Document TD-Shooter

## 1. Spielüberblick

- Genre: Shooter
- Ziel des Spiels: So viel Score wie möglich erzielen.
- Zielplattform: Windows
- Zielgruppe: Jugendliche und junge Erwachsene

## 2. Gameplay und Regeln

- Spielfigur: Bewegung, Leben, Geschwindigkeit
- Gegner: Typen, Verhalten (z.B. verfolgen, schiessen)
- Steuerung: Tasten für Bewegung, Schiessen, Pause
- Punkte/Score: Wie erhält man Punkte? Highscore?
- Spielende: Wann ist verloren / gewonnen? Restart?

## 3. Level und Content

- Anzahl Level (für MVP): 2
- Levelaufbau:
  - Grösse: 16'000 x 8'000
  - Layout: Viele Hindernisse
- Schwierigkeit: Anzahl Score

## 4. Benutzeroberfläche (UI/UX)

- Hauptscreen:
  - Spielfeld: Spielre, Gegner
  - UI/ UX: Leben, Score und Zeit
- Start-/Endbildschirm: Starten, Steuerung und Beenden
- Siehe Dokument:

## 5. Technisches Konzept / Architektur

- Technologie: Python-Version, Libraries (z.B. pygame)
- Hauptmodule/Klassen:
  - Game Loop
  - Player
  - Enemy
  - Bullet/Projectile
  - Level/Map

## 6. Nicht-funktionale Anforderungen

- Performance: mind. 50 Gegner auf einmal mit guter Performance.
- Bedienbarkeit: Window
- Portabilität: mind. Mid-Range CPU

## 7. Abnahmekriterien (Aus Sicht BA/AG)

- Das Spiel gilt als fertig, wenn End-Level erreicht und der Spieler stirbt.
- Der Spieler kann sich in vier Richtungen bewegen.
- Mindestens zwei Level ist komplett durchspielbar.
- Score wird angezeigt und nach Game Over bleibt sichtbar.
- Eigenständiges .exe-Datei.
