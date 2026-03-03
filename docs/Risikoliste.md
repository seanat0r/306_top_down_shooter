# Risikoliste TD-Shooter
Stand: 03.03.2026

Legende:
- W = Wahrscheinlichkeit (niedrig / mittel / hoch)
- A = Auswirkung (niedrig / mittel / hoch)

---

## R1 – Zeit reicht für Initialisierung/Konzept nicht aus
- Beschreibung: Umfang der Aufgaben (PIA, Stakeholderliste, Risikoliste, GDD, PMP) sprengt das verfügbare Zeitfenster.
- W: mittel
- A: hoch
- Massnahmen:
  - Klare Agenda und Timeboxing pro Teilaufgabe.
  - Offene Punkte als To-dos für später festhalten.
  - Fokus zuerst auf Pflichtdokumente für Meilenstein.

## R2 – Unklarer Scope / MVP des Spiels
- Beschreibung: Team einigt sich nicht auf ein realistisches MVP; es werden zu viele Features geplant.
- W: mittel
- A: hoch
- Massnahmen:
  - MVP im GDD schriftlich festhalten (1 Level, Basis-Features).
  - PL entscheidet bei Unklarheiten.
  - Erweiterungen nur über dokumentierte Change Requests.

## R3 – Technische Probleme mit Python / EXE / GitHub
- Beschreibung: Probleme mit Entwicklungsumgebung, Libraries, EXE-Build oder GitHub-Workflow verzögern die Umsetzung.
- W: mittel
- A: mittel
- Massnahmen:
  - Früh ein Minimalprojekt („Hello World“-Spiel) erstellen und bis EXE/Run testen.
  - GitHub-Zugriff und Branching vorab prüfen.
  - Technische Issues sofort erfassen, priorisieren und einem DEV zuweisen.

## R4 – Ausfall von Teammitgliedern
- Beschreibung: Krankheit oder Ausfall eines Teammitglieds führt zu Engpässen bei Code oder Dokus.
- W: niedrig
- A: hoch
- Massnahmen:
  - Aufgaben und Wissen verteilen (kein Single Point of Failure).
  - GitHub konsequent nutzen (Code, Dokus, Protokolle aktuell halten).
  - Backup-Verantwortliche pro Rolle definieren (z.B. 2. DEV, 2. QA).

## R5 – ungenügende Testabdeckung
- Beschreibung: Zu wenig Zeit für Tests, Fehler fallen erst bei Abnahme auf.
- W: mittel
- A: mittel
- Massnahmen:
  - Einfaches Testkonzept früh erstellen.
  - Smoke-Tests nach jedem grösseren Merge.
  - QA-Check vor Meilensteinen einplanen.