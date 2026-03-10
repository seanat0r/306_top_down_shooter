# Game Design Document TD-Shooter

## Inhaltsverzeichnis

1. [Grobspezifikation & Anforderungen](#1-grobspezifikation--anforderungen)\
  1.1[Spielüberblick](#11-spielüberblick)\
  1.2[Gameplay und Regeln](#12-gameplay-und-regeln)\
  1.3[Level und Content](#13-level-und-content)\
  1.4[Benutzeroberfläche (UI/UX)](#14-benutzeroberfläche-uiux)\
  1.5[Technisches Konzept / Architektur](#15-technisches-konzept--architektur)\
  1.6[Nicht-funktionale Anforderungen](#16-nicht-funktionale-anforderungen)\
  1.7[Abnahmekriterien (Aus Sicht BA/AG)](#17-abnahmekriterien-aus-sicht-baag)
2. [Spiellogik](#2-spiellogik)\
  2.1[Gameplay Loop](#21-gameloop)\
  2.2[Entity](#22-entity)\
  2.3[Architektur](#23-architektur)

## 1. Grobspezifikation & Anforderungen

### 1.1 Spielüberblick

- Genre: Shooter
- Ziel des Spiels: So viel Score wie möglich erzielen.
- Zielplattform: Windows
- Zielgruppe: Jugendliche und junge Erwachsene

### 1.2 Gameplay und Regeln

- Spielfigur: Bewegung, Leben, Geschwindigkeit
- Gegner: Typen, Verhalten (z.B. verfolgen, schiessen)
- Steuerung: Tasten für Bewegung, Schiessen, Pause
- Punkte/Score: Wie erhält man Punkte? Highscore?
- Spielende: Wann ist verloren / gewonnen? Restart?

### 1.3 Level und Content

- Anzahl Level (für MVP): 2
- Levelaufbau:
  - Grösse: 16'000 x 8'000
  - Layout: Viele Hindernisse
- Schwierigkeit: Anzahl Score

### 1.4 Benutzeroberfläche (UI/UX)

- Hauptscreen:
  - Spielfeld: Spielre, Gegner
  - UI/ UX: Leben, Score und Zeit
- Start-/Endbildschirm: Starten, Steuerung und Beenden
- Siehe Dokument: `./docs/skizze_benutzeroberfläche.jpg`

![A prototype of the UI](./images/skizze_benutzeroberfläche.jpg "A Basic UI")

### 1.5 Technisches Konzept / Architektur

- Technologie: Python-Version, Libraries (z.B. pygame)
- Hauptmodule/Klassen:
  - Game Loop
  - Player
  - Enemy
  - Bullet/Projectile
  - Level/Map

### 1.6 Nicht-funktionale Anforderungen

- Performance: mind. 50 Gegner auf einmal mit guter Performance.
- Bedienbarkeit: Window
- Portabilität: mind. Mid-Range CPU

### 1.7 Abnahmekriterien (Aus Sicht BA/AG)

- Das Spiel gilt als fertig, wenn End-Level erreicht und der Spieler stirbt.
- Der Spieler kann sich in vier Richtungen bewegen.
- Mindestens zwei Level ist komplett durchspielbar.
- Score wird angezeigt und nach Game Over bleibt sichtbar.
- Eigenständiges .exe-Datei.

## 2. Spiellogik

### 2.1 Gameloop

Gameloop besteht hauptsächlich aus einem Spieler der gegen Gegner schiessen muss. Pro getöteter Gegner gibt es +1 Score.
Das Ziel ist es so lange wie möglich und bis mind. Level 2 zu erreichen.

### 2.2 Entity

#### Spieler

Der Spieler hat folgende Eigenschaften:

- **Leben**: max. 3
- **Munition**: Die Anzahl schüsse, bis es wieder die Waffe aufladen muss. Das Nachladen erfolgt Automatisch oder mit einer Tasten druck manuell.
- **Score**: Der Score anzahl, grundsätzlich pro getöteter Gegner.
- **Waffe**: Eine Schusswaffe.

#### Gegner

Der gegner hat folgende Eigenschaften:

- **Leben**: Die Gegner haben bassierend auf der Zeit immer mehr Lebenspunkte. Gestartet wird mit 3 Lebenspunkten.
- **Nahkampfschaden**: Wenn ein Gegner den Spieler berührt, wird ein Schaden an den Spieler verursacht.
- **Bei Tod**: Beim Tod erhält der Spieler ein Score.
- **Bewegung**: Die Gegner Bewegung der Gegner verfolgen der Spieler.

#### Schuss

Der Schuss ist ein kleines Projektill, das Schaden an Gegner verursacht.

- **Bei Berührung bei...**
  - **Umgebung/ Hindernisse**: Der Schuss wird zerstört.
  - **Gegner**: Der Schuss versuacht ein Schaden bei Gegner und gibt den Gegner einen kleinen Rückstoss beim Gegner.

#### Umgebung

Die Umgebung der Levels wird von Hand erstellt. Die Umgebung haben diverse Hindernisse die weder Spieler, Gegner und Schüsse durchlassen.

##### Level 1

Dort sollte es wenig Hindernisse geben um die Schwierigkeit etwas einfacher zu halten. Es sollte gleichzeitig als kleines Tutorial dienen, um den Spieler mit der Steuerung und der grundlegender Gameloop vertraut zu machen.

##### Level 2

Hier wird das Level mit mehr Hindernisse erstellt, um die Schwierigkeit schwieriger gestallten. Gedacht wäre Dead-Ends um Spieler in die Zwickmühle zu bringen.

### 2.2 UI

Das UI/ UX besteht aus 4 Kern Elementen.

1. Die Lebensanzeige
2. Der Score
3. Die Munitionsanzeige
4. Spielfeld

Die Lebensanzeige wird oben links horizontal auf dem Bildschirm dargestellt. Unterhalb davon kommt die Score anzeige, ebensfalls horizontal.
Die Munitionsanzeige kommt unten rechts als vertikaler Balken. Das Spielfeld ist der Restlicher teil.

![Image showing the UI of the game](./images/Benutzeroberfläche_finale.png "The final UI")

### 2.3 Architektur

Das Spiel wird nach dem EVA-Prinzip (Eingabe, Verarbeitung, Ausgabe) strukturiert und nutzt eine klassenbassierte Architektur:

- **Game-Klasse (Controller)**: Verwaltet den Main-Loop, die Events (Tastatur) und den Wechsel zwischen den Levels.
- **Sprite-System**: Nutzung der `pygame.sprite.Sprite` Basisklasse für:
  - `Player`: Enthällt HP-Managment und Bewegungslogik.
  - `Enemy`: Enthält die Verfolgungs-KI und Schadensberechnung.
  - `Projectile`: Berechnet die Flugbahn und Kollision mit Hindernissen.
- **Level-Manager**: Lädt die Map-Daten (Hindernissse) und platziert die Entities.
- **UI-Manager**: Zeichnet das HUD über das Spielfeld.
