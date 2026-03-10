# Projektmanagementplan (PMP) – TD‑Shooter

Dieser Plan beschreibt die Steuerung und Umsetzung des Projekts **TD‑Shooter** im Rahmen des Moduls 306A, basierend auf der Methode **HERMES 5** (Szenario: Kleinprojekt).

## 1. Phasen, Zeitplan und Meilensteine

Das Projekt ist auf eine Laufzeit von ca. 6 Tagen ausgelegt und folgt dem Phasenmodell für Kleinprojekte.

| Phase             | Zeitraum   | Fokus & Aktivitäten                                            | Meilenstein (Entscheid)          |
| :---------------- | :--------- | :------------------------------------------------------------- | :------------------------------- |
| **Initialisierung**| 03.03.2026 | Projektstart, Repository-Setup, PIA, Stakeholder & Risiken    | **M1: Projektfreigabe** |
| **Konzept** | Tag 2      | Erstellung GDD, PMP, Teststrategie und Architekturplan         | **M2: Konzeptfreigabe** |
| **Realisierung** | Tag 3 – 4  | Iterative Entwicklung, Feature-Implementierung, Testprotokolle | **M3: Lauffähiger Prototyp** |
| **Einführung** | Tag 5 – 6  | Abnahmetests, EXE-Release, Abschlussbericht & Präsentation     | **M4: Schlussabnahme** |

## 2. Projektorganisation und Rollen

Das Team verteilt die Rollen gemäss HERMES-Standard, angepasst auf die Teamgrösse von vier Personen.

| Rolle | Person | Hauptaufgaben |
| :--- | :--- | :--- |
| **Projektleitung (PL)** | Stefanie Gerber | Termine, Scope, Risiko-Management, Stakeholder-Kommunikation. |
| **Business Analyst (BA)**| Christophe Grädel | Anforderungen, GDD-Pflege, Definition der Abnahmekriterien. |
| **Entwicklung (DEV)** | Benjamin Phengrasamy | Software-Architektur, Implementation (Python/Pygame), Build-Prozess. |
| **Qualitätssicherung (QA)**| Sujanthan Suntheralingam | Testkonzept, Testprotokolle, Durchführung der Abnahmetests. |

> **Stellvertretung:** Jede Kernaufgabe wird durch eine zweite Person mitverfolgt. Die laufende Dokumentation im GitHub-Repository stellt sicher, dass das Projekt auch bei Ausfällen fortgeführt werden kann.

## 3. Planung und Steuerung

Die Steuerung erfolgt aktiv über das Repository und tägliche Abstimmungen.

- **Daily Sync:** Ein kurzes 5–10 minütiges Meeting zu Beginn jedes Kurstages (Fortschritt, Blocker, Tagesziele).
- **Task-Management:** Alle Aufgaben werden als **GitHub-Issues** erfasst (inkl. Zuweisung und Zieltermin).
- **Versionskontrolle:** Nutzung von **Feature-Branches**. Änderungen werden ausschliesslich via Pull-Requests nach einem Review in den `main`-Zweig gemergt.
- **Berichterstattung:** Die PL erstellt während der Realisierung Statusberichte und informiert den Auftraggeber bei Meilensteinen.

## 4. Qualitätssicherung

Um eine gleichbleibende Qualität sicherzustellen, gilt die folgende **Definition of Done (DoD)** für jeden Arbeitsauftrag:

- Code ist im Repository eingecheckt und fehlerfrei ausführbar.
- Die Funktionalität wurde gemäss Anforderungen getestet.
- Dokumentation (GDD, Testprotokoll) wurde bei Bedarf aktualisiert.
- Mindestens ein Peer-Review durch ein anderes Teammitglied wurde durchgeführt.

Die HERMES-Dokumente (PIA, PMP, Testkonzept etc.) werden im Verzeichnis `/docs` gepflegt und gegengelesen.

## 5. Kommunikation

| Kanal | Empfänger | Zweck |
| :--- | :--- | :--- |
| **Präsenz / Daily** | Team | Koordination der täglichen Aufgaben und Probleme. |
| **MS Teams / Discord** | Team | Kommunikation im Homeoffice oder bei dringenden Fragen. |
| **GitHub Issues/PRs** | Team | Dokumentation technischer Entscheidungen und Code-Reviews. |
| **Präsentationen** | Auftraggeber | Abnahme der Meilensteine M1 bis M4. |

## 6. Risiko- und Change‑Management

### Risiko-Management

Risiken werden nach Eintrittswahrscheinlichkeit (W) und Schadensausmass (S) auf einer Skala von 1 (niedrig) bis 3 (hoch) bewertet.

| Risiko | W | S | Massnahme |
| :--- | :--- | :--- | :--- |
| Zeitknappheit | 3 | 3 | Konzentration auf MVP (Minimum Viable Product); "Nice-to-haves" streichen. |
| Technische Hürden | 2 | 2 | Frühzeitige Spikes/Prototypen für komplexe Mechaniken. |
| Ausfall Teammitglied | 1 | 3 | Strikte Dokumentation und Code-Reviews zur Wissensverteilung. |

### Change-Management

Anpassungen am Scope oder den Anforderungen werden als **Change-Requests** behandelt:

1. Erfassung als GitHub-Issue mit Label `change`.
2. Diskussion im Team über Auswirkungen auf Zeit und Ressourcen.
3. Entscheid durch die Projektleitung in Abstimmung mit dem Auftraggeber.
