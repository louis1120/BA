# Messung

Für die Bewertung, wie gut lokale LLMS die Repository-Gesundheit einverbessern, wurde ein Prototyp gebaut, welcher sich aufgrund der zeitlichen Rahmenbedingungen auf Aufgaben fokussiert.
Da Modelle bei größerem Kontext länger rechnen und ungenauer werden, wurde sich hier auf den Umfang eines PullRequests begrenzt. - Quelle
Die Aufgaben sind, die Erstellung einer PullRequest Beschreibung und das Prüfen von den Änderungen eines PRs.
- genauer drauf eingehen und erklären was sind codediffs usw.
Für das Erstellen der Beschreibung eines PRs bekommt das LLM eine spezifische Prompt, sowie die zusammengefassten Codediffs, sowie alle Commit Messages, als Context.
Das Code-Review des PRs funktioniert ähnlich, wobei jedoch ein andere Prompt verwendet wird und nur der Codediff.
