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
| -"- S.13451 | Kommentare entfernen | wenn es nicht wichtig ist, werden kommentare entfernt | Jenachdem was ich messen, will sollte ich dei Daten anpassen, denn je länger der Context, desto ungenauer wird es (beweis finden) |
| -"- S.1349 | LLM-Based Code Refactoring - Prompt für Analysis | Prompt:  Instructions, Definitions Code | Kann basis für aufbau eigener Prompts sein => je nachdem was gemessen wird die Definitions und Instructions anpassen|
|  https://arxiv.org/pdf/2107.03374 |  samples |  "Real-world programming tasks often involve iterations of approaches and bug fixes, which is approximated by generating many samples from our models and selecting one that passes all unit tests." | Spannend für architektur, problem ist jedoch die rechenzeit. ( Mehrere Modelle parallel oder das eine Konzept wo es einen gibt eder erstellt und einen der Bewertet) - Spannend wäre es sich den entwicklungsprozess von menschen anzuschauen und zu schauen wie man den mit MAA nachbauen kann                            |
| https://arxiv.org/pdf/2402.01030 | logische Komponente hinzufügen | Table 5 zeigt wie CodeAct kleine Modelle verbessert | Beispiel CodeAct: Es gibt einen CodeAgent, der bei logischen Anfragen code entiwckelt und diesen ausführt, da LLMs als Sprachverarbeitende Modelle das nicht gut könne, vor allem die kleinen| 
| https://arxiv.org/pdf/2210.03629 | Reasoning und Acting |  | Durch die kombination von Reasoningmodellen und Aktionen, kann ich Schlussfolgern, welche Funktion jetzt sinn machen würde bevor ich sie ausführe|
| https://openreview.net/pdf?id=yzkSU5zdwD S.10f | Potenziale für weiterentwicklung verbesserung von LLMs | / | Skalierung des Modells, Architektur verbessern und Trainieren, Daten skalieren, Prompten meistern, ... Spannend, aber für das Tool nur als Negtaivbeispiel nützlich, was kann ich nicht verbessern, wo sind meine Grenzen |
| https://arxiv.org/pdf/2210.03629 | Extract Knowledge | | Mithilfe einer Wissensdatenbank oder der GitHubApi könnte das Tool nach anderen Repositories suchen und diese vergleichen, um z.b. die Codepatterns oder Commitnachrichten nach einem bestimmten musster zu erstellen und nicht wie es traineirt wurde|
| https://arxiv.org/pdf/2501.04227 | Multi-Agenten-System | | Es wird ein MAS genutzt wobei verschiedene Agenten eine Peer-Diskussion widerspiegeln, dass könnte man so ähnlich auch nachbilden, dass mehrere agenten die ergebnisse diskuttieren|
###### Wie kann ich meine Ergebnisse Evaluieren?

| **Zitation** | **Art** | **Erklärung** | **Anmerkung/Relevanz für meine Arbeit** |
|-------------|----------|------------|----------------------------------------|
| https://ieeexplore.ieee.org/document/10764947/ | Research Questions | Definieren von RQ, Testdaten entwickeln die alles abdecken, mehrere LLMs um vergleich zu haben, Temperatur = 0,2, Response Token < 1500 | Sehr sinnvolle Methode, welche ich gut auf meinen UC anwenden kann| 
| https://arxiv.org/pdf/2107.03374 |  vergleichen vershciedener Modelle | sie nutzen HumanEval(haben es scheinbar erstellt) um die LLMs zu testen  |      Einerseits vergleich von Qwen und deepsekk andererseits wäre ein vergleich mit den besten modellen über z.b. Api auch spannend wenn es geht                       |
| https://openreview.net/pdf?id=yzkSU5zdwD S.3 |  Benchmarking with Few-ShotPrompting |  Ich gebe dem Modell einige Aufgaben mit gewünschten output bevor ich meine Aufgabe stelle |         Sicherlich sinnvoll für kleinere Codeabschnitte, jedoch nicht zwingend gebrauchbar für das Tool                    |
| https://arxiv.org/pdf/2210.03629 | Qualitativ | | Ich vergleiche die Ausgabe direkt miteinander und zeige anhand der unterschiede was inhaltlich besser geworden ist|

###### Wie kann man das Tool weiterenetiwckeln? 
| **Zitation** | **Thema** | **Aussage** | **Anmerkung/Relevanz für meine Arbeit** |
|-------------|----------|------------|----------------------------------------|
| https://ieeexplore.ieee.org/document/10851473 S. 140 |  Realtime Feedback direkt im DevCycle|  Zwischen dem Öffnen eines PR und dem Mergen wird mittels eines LLM Evaluiert| Würde nicht mehr Lokal laufen wäre aber automatisiert | 
| https://ieeexplore.ieee.org/document/10851473 S. 141 |  Issues tracking integration | es werden automatisch issues oder tickets z.b. in jira erstellt| serh gute idee, da man viel finden wird und es dann irgendwo direkt dokumentiert hat und auch andere es bearbeiten können | 



###### Sonstiges 
| **Zitation** | **Thema** | **Aussage** | **Anmerkung/Relevanz für meine Arbeit** |
| https://openreview.net/pdf?id=yzkSU5zdwD S.8f. - Ursprungs Quelle (Weidinger et al., 2021)| Verzerrung/ Toxizität | Aus Weidinger nehmen | Verzerrung, Toxizität können Antworten beeinflussen |
| https://arxiv.org/pdf/2206.06336 | Universelle Aufgabenschnittstelle durch Sprachmodelle | Sprachmodelle dienen als universelle Schnittstelle für verschiedene Aufgaben und Modalitäten | Unterstützt die Idee, LLMs als Kern für die Analyse der Repository-Gesundheit zu nutzen |



