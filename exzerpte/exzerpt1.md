
### Ziele
Wonach suche ich?
- Fragestellungen und antworten
Wie ist Begriff X definiert?
Was ist der Standpunkt zu Thema ?
Wie ist der Forschungsstand zu Thema X?
Direktzitate
Informationen
###### Wie ist der Forschungsstand zu Repository analyse mittels lokalen LLMs?
| **Zitation** | **Thema** | **Aussage** | **Anmerkung/Relevanz für meine Arbeit** |
|-------------|----------|------------|----------------------------------------|
| https://ieeexplore.ieee.org/document/10851473  | Security  |  Identifikation von Schwachstellen und Antipattern mittel KI | ALs Forschungsstand, das gibt es auch.../ ALs Beispiel wie man es weiterentwickeln könnte oder als Vorbild einer Metrik                      |

###### Wie kann ich mithilfe von LLMs Repository-Gesundheit messen?
| **Zitation** | **Thema** | **Aussage** | **Anmerkung/Relevanz für meine Arbeit** |
|-------------|----------|------------|----------------------------------------|
|  |   |   |                             |


###### Wie kann ich durch ein MoE/ einem Multiagentensystem und anderen Technologien die Kompetenz erhöhen?

| **Zitation** | **Thema** | **Aussage** | **Anmerkung/Relevanz für meine Arbeit** |
|-------------|----------|------------|----------------------------------------|
|  https://ieeexplore.ieee.org/document/10764947/ |  Smell Detection via MoE |  Nutzt MoE zur entscheidung, welches Code-Smell Tool aufgerufen werden soll |   MoE ist ein möglicher Ansatz den man verfolgen könnte, Training und Fine-Tuning ist wahrscheinlich zu rechenintensiv                          |
| -"- S.1349 | LLM-Based Code Refactoring - Prompt für Refactoring | Prompt: besteht aus Instructions, Definitions für jeden Code-Smell-Typ ,Refactoring Examples, dem Untersuchten Code und dem Code-Smell selber/ der ausgabe aus dem Tool davor | Kann basis für aufbau eigener Prompts sein|
| -"- S.1349 | Code Refactoring auf Methoden oder Klassenebene | Klassenebene über mehrere Dateien/Klassen hinweg => Subprozess damit wir besser refactoren können, Methodenebene => LLM kann es direkt machen | Ansatz kann für meine Architektur sinnvoll sein, da einfache 7-14b LLMs noch weniger können und daher mit Klassenebene sicher überfordert sind|
| -"- S.1351 | Kommentare entfernen | wenn es nicht wichtig ist, werden kommentare entfernt | Jenachdem was ich messen, will sollte ich dei Daten anpassen, denn je länger der Context, desto ungenauer wird es (beweis finden) |
| -"- S.1349 | LLM-Based Code Refactoring - Prompt für Analysis | Prompt:  Instructions, Definitions Code | Kann basis für aufbau eigener Prompts sein => je nachdem was gemessen wird die Definitions und Instructions anpassen|
|  https://arxiv.org/pdf/2107.03374 |  samples |  "Real-world programming tasks often involve iterations of approaches and bug fixes, which is approximated by generating many samples from our models and selecting one that passes all unit tests." | Spannend für architektur, problem ist jedoch die rechenzeit. ( Mehrere Modelle parallel oder das eine Konzept wo es einen gibt eder erstellt und einen der Bewertet) - Spannend wäre es sich den entwicklungsprozess von menschen anzuschauen und zu schauen wie man den mit MAA nachbauen kann                            |

###### Wie kann ich meine Ergebnisse Evaluieren?

| **Zitation** | **Art** | **Erklärung** | **Anmerkung/Relevanz für meine Arbeit** |
|-------------|----------|------------|----------------------------------------|
| https://ieeexplore.ieee.org/document/10764947/ | Research Questions | Definieren von RQ, Testdaten entwickeln die alles abdecken, mehrere LLMs um vergleich zu haben, Temperatur = 0,2, Response Token < 1500 | Sehr sinnvolle Methode, welche ich gut auf meinen UC anwenden kann| 
| https://arxiv.org/pdf/2107.03374 |  vergleichen vershciedener Modelle | sie nutzen HumanEval(haben es scheinbar erstellt) um die LLMs zu testen  |      Einerseits vergleich von Qwen und deepsekk andererseits wäre ein vergleich mit den besten modellen über z.b. Api auch spannend wenn es geht                       |
|  |   |   |                             |
|  |   |   |                             |
###### Wie kann man das Tool weiterenetiwckeln? 
| **Zitation** | **Thema** | **Aussage** | **Anmerkung/Relevanz für meine Arbeit** |
|-------------|----------|------------|----------------------------------------|
| https://ieeexplore.ieee.org/document/10851473 S. 140 |  Realtime Feedback direkt im DevCycle|  Zwischen dem Öffnen eines PR und dem Mergen wird mittels eines LLM Evaluiert| Würde nicht mehr Lokal laufen wäre aber automatisiert | 
| https://ieeexplore.ieee.org/document/10851473 S. 141 |  Issues tracking integration | es werden automatisch issues oder tickets z.b. in jira erstellt| serh gute idee, da man viel finden wird und es dann irgendwo direkt dokumentiert hat und auch andere es bearbeiten können | 


https://arxiv.org/pdf/2107.03374
