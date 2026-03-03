# Game Design

## Inhaltsverzeichnis

1. [Spiellogik](#1-spiellogik)
2. [UI](#2-ui)
3. [Architektur](#3-architektur)

## 1. Spiellogik

### Gameloop

Gameloop besteht hauptsächlich aus einem Spieler der gegen Gegner schiessen muss. Pro getöteter Gegner gibt es +1 Score.
Das Ziel ist es so lange wie möglich und bis mind. Level 2 zu erreichen.

### Entity

#### Spieler

Der Spieler hat folgende Eigenschaften:

- **Leben**: max. 3
- **Munition**: Die Anzahl schüsse, bis es wieder die Waffe aufladen muss.
- **Score**: Der Score anzahl, grundsätzlich pro getöteter Gegner.
- **Waffe**: Eine Schusswaffe.

#### Gegner

Der gegner hat folgende Eigenschaften:

- **Leben**: Die Gegner haben bassierend auf der Zeit immer mehr Lebenspunkte. Gestartet wird mit 3 Lebenspunkten.
- **Nahkampfschaden**: Wenn ein Gegner den Spieler berührt, wird ein Schaden an den Spieler verursacht.
- **Bei Tod**: Beim Tod erhält der Spieler ein Score.

#### Schuss

Der Schuss ist ein kleines Projektill, das Schaden an Gegner verursacht.

- **Bei Berührung bei...**
  - **Umgebung/ Hindernisse**: Der Schuss wird zerstört.
  - **Gegner**: Der Schuss versuacht ein Schaden bei Gegner.

### Umgebung

Die Umgebung der Levels wird von Hand erstellt. Die Umgebung haben diverse Hindernisse die weder Spieler, Gegner und Schüsse durchlassen.

#### Level 1

Dort sollte es wenig Hindernisse geben um die Schwierigkeit etwas einfacher zu halten. Es sollte gleichzeitig als kleines Tutorial dienen, um den Spieler mit der Steuerung und der grundlegender Gameloop vertraut zu machen.

#### Level 2

Hier wird das Level mit mehr Hindernisse erstellt, um die Schwierigkeit schwieriger gestallten. Gedacht wäre Dead-Ends um Spieler in die Zwickmüjle zu bringen.

## 2. UI


## 3. Architektur