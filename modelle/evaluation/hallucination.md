


# Evaluation von Halluzinationen

## Literatur
Mögliche Papers zum Thema:
- https://arxiv.org/pdf/2404.00971
- https://arxiv.org/pdf/2407.09726
- https://arxiv.org/pdf/2403.04307v3

### 1. Definition von Halluzinationsmetriken

Anstatt jede einzelne generierte Ausgabe aufzulisten, sollten messbare Aspekte von Halluzinationen definiert werden:

- **Erfundene Inhalte**: Informationen, die nicht im Repository vorhanden sind (z. B. nicht existierende Funktionen oder Abhängigkeiten).
- **Überverallgemeinerung**: Aussagen, die weit über den Inhalt des Repositories hinausgehen (z. B. "Dieses Framework unterstützt alle Datenbanken", wenn nur SQLite verwendet wird).
- **Falsche Struktur**: Sektionen, die erstellt werden, obwohl keine relevanten Informationen im Repository vorhanden sind (z. B. eine "Contributing"-Sektion ohne Beitragsrichtlinien).
- **Falsche Attribution**: Fehlzuordnungen von Technologien, Lizenzen oder Autorenschaft.

Jeder dieser Halluzinationstypen sollte durch konkrete Beispiele in einem Evaluierungsdatensatz belegt werden.

### 2. Stichproben- und Evaluierungsstrategie

Da es unpraktisch ist, jede generierte Ausgabe einzeln zu überprüfen, sollte eine gezielte Evaluierungsstrategie angewendet werden:

- **Zufällige Stichprobe**: Auswahl einer diversen Teilmenge von Repositories, die unterschiedliche Faktoren wie Größe, Programmiersprache und Vollständigkeit abdecken.
- **Manuelle Überprüfung**: Abgleich der generierten Dokumentation mit dem tatsächlichen Repository-Inhalt.
- **Quantitative Bewertung**: Erfassen der Anzahl von Halluzinationen pro Kategorie und Berechnung folgender Kennzahlen:
    - **Halluzinationsrate** = (Anzahl der halluzinierten Fakten) / (Gesamtanzahl der faktischen Behauptungen)
 

### 3. Qualitative Analyse

Zusätzlich zur quantitativen Auswertung ist eine detaillierte qualitative Analyse erforderlich:

- **Repräsentative Beispiele**: Darstellung einzelner Fälle mit besonders guter oder schlechter Performance.
- **Fehlermuster**: Identifikation häufiger Ursachen für Halluzinationen (z. B. das Fehlen einer LICENSE-Datei führt zu erfundenen Lizenzangaben).
- **Modellverhalten**: Untersuchung von Situationen, in denen Halluzinationen besonders häufig auftreten (z. B. wenn wichtige Metadaten fehlen).
-  **Aufgabenbereich**: Ist z.B. die Erweiterung oder Erstellung von Dokumentation anfälliger als Code-Analyse? 

### 4. Ergebnispräsentation

Zur klaren Darstellung der Ergebnisse sollten verschiedene visuelle und analytische Mittel eingesetzt werden:

- **Tabellen und Diagramme**: Darstellung der Häufigkeit von Halluzinationen, der Typen und der Modellgenauigkeit.
- **Boxplots**: Visualisierung der Verteilung der Korrektheitswerte.

Für tiefere Erkenntnisse könnten zusätzliche Elemente wie Heatmaps zur Fehlerverteilung oder eine zeitliche Analyse der Modellverbesserung herangezogen werden.
