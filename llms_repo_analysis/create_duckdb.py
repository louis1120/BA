import duckdb

# Verbindung zur DuckDB-Datenbank (erstellt Datei, falls nicht vorhanden)
db = duckdb.connect("llm_analysis.db")

# Tabellen erstellen
db.execute("""
CREATE TABLE IF NOT EXISTS Prompts (
    prompt_id INTEGER PRIMARY KEY,
    prompt_text TEXT,
    specificity INTEGER
);
""")

db.execute("""
CREATE TABLE IF NOT EXISTS CodeDiffs (
    diff_id INTEGER PRIMARY KEY,
    diff_text TEXT,
    language TEXT,
    change_type TEXT
);
""")

db.execute("""
CREATE TABLE IF NOT EXISTS GeneratedMessages (
    message_id INTEGER PRIMARY KEY,
    prompt_id INTEGER REFERENCES Prompts(prompt_id),
    diff_id INTEGER REFERENCES CodeDiffs(diff_id),
    model TEXT,
    generated_output TEXT,
    response_time REAL,
    metric TEXT
);
""")

db.execute("""
CREATE TABLE IF NOT EXISTS Evaluations (
    evaluation_id INTEGER PRIMARY KEY,
    message_id INTEGER REFERENCES GeneratedMessages(message_id),
    evaluation_method TEXT CHECK(evaluation_method IN ('human_feedback', 'deepeval')),
    answer_relevancy REAL,
    hallucination_rate REAL,
    prompt_alignment REAL
);
""")

print("DuckDB-Datenbank erfolgreich erstellt und mit Beispiel-Daten gefüllt! 🚀")

# Verbindung schließen
db.close()
