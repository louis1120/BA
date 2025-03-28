import duckdb
import typer

def create_duckdb():
    db = duckdb.connect("llm_analysis.db")

    db.execute("""
    CREATE TABLE IF NOT EXISTS Prompts (
        prompt_id UUID PRIMARY KEY,
        prompt_text TEXT,
        metric TEXT
    );
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS CodeDiffs (
        pr_id UUID PRIMARY KEY,
        diff_text TEXT,
        commit_messages TEXT,
        repository TEXT,
        language TEXT,
        pr_number INT
    );
    """)

    db.execute(""" 
    CREATE TABLE IF NOT EXISTS GeneratedMessages (
        message_id UUID PRIMARY KEY,
        prompt_id UUID REFERENCES Prompts(prompt_id),
        pr_id UUID REFERENCES CodeDiffs(pr_id),
        model TEXT,
        generated_output TEXT,
        total_duration REAL,
        load_duration REAL,
        prompt_tokens INTEGER,
        prompt_eval_time REAL,
        generated_tokens INTEGER,
        generation_time REAL
    );
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS Evaluations (
        evaluation_id UUID PRIMARY KEY,
        message_id UUID REFERENCES GeneratedMessages(message_id),
        evaluation_method TEXT,
        evaluation_model TEXT,
        answer_relevancy REAL,
        faithfulness REAL,
        prompt_alignment REAL
    );
    """)

    typer.echo("DuckDB created!🚀")

    db.close()

