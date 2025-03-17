# Aufbau

Der Prototyp interagiert mit einer laufenden Ollamainstanz, sowie mit Github. 
Für die Messungen wurde DuckDB zum speichern der Daten verwendet.
Der Nutzer muss, wenn er eine PR-Beschreibung will, das Zielrepository, sowie die PR-Nummmer angeben.
Darrauffolgend kann der Nutzer ein LLM auswählen, welches er zur Generierung verwenden will.
Anschließend werden die Codediffs, sowie die Commitmessages des PRs aus Github genommen und zu dem Prompt hinzugefügt.
Danach wird mittels des ausgewählten Models die lokale Ollamainstanz getriggert.
Nach durchschnittlich wird dann eine ausgabe ausgegeben.