# Messung

Für die Bewertung, wie gut lokale LLMS die Repository-Gesundheit einverbessern, wurde ein Prototyp gebaut, welcher sich aufgrund der zeitlichen Rahmenbedingungen auf Aufgaben fokussiert.
Da Modelle bei größerem Kontext länger rechnen und ungenauer werden, wurde sich hier auf den Umfang eines PullRequests begrenzt. - Quelle
Die Aufgaben sind, die Erstellung einer PullRequest Beschreibung.
- genauer drauf eingehen und erklären was sind codediffs usw.
Für das Erstellen der Beschreibung eines PRs bekommt das LLM eine spezifische Prompt.
Es wurden 3 verscheidenen Prompts erstellt, welche den zusammengefassten Codediff, sowie alle Commit Messages beinhalten.
Der erste Prompt richtet sich nach dem Prinzip des few-shots learing hier werden einige beispiele vorgegeben, an den sich das LLM richten soll.
###### Unleashing the potential of prompt engineering in Large Language Models: a comprehensive review S.11
Der nächste Prompt verfolgt das Prinzip der structured chain of thought.
###### Unleashing the potential of prompt engineering in Large Language Models: a comprehensive review S.6
Hier wird dem LLM einen Schritt für Schritt Anleitung vorgegeben.
Die dritte Promptvariation vereinigt die beiden Konzepte.
Neben den verschiedenen Promptvariationen wurden pro LLM zwei verschiedene Temperaturen gewählt, um zu schauen, ob diese Einfluss auf die Ergebnisse hat.
Es wurden drei Wiederholungen bei den Messungen pro Variante gemacht, um die Genauigkeit der Ergebnisse zu erhöhen und mögliche Messfehler(Außreißer) zu minimieren.
Zusammengefasst addieren sich so 36 Varianten pro PR auf.
Aufgrund von Zeitmangel, sowie Energieverbrauch, wurden 40 PR ausgewählt.
Somit wurden 1440 Messungen durchgeführt.
Anschließend wurden die gemessenen Ergebnisse Evaluiert. - Siehe Evaluation
<!-- Das Code-Review des PRs funktioniert ähnlich, wobei jedoch ein andere Prompt verwendet wird und nur der Codediff. -->
