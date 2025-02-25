import uuid
import duckdb

db = duckdb.connect("llm_analysis.db")

def insert_codediff(diff_text, language):
    """
    Generates a UUID and stores the code diff in the CodeDiffs table.
    """
    diff_id = str(uuid.uuid4())
    db.execute("INSERT INTO CodeDiffs (diff_id, diff_text, language) VALUES (?, ?, ?)", (diff_id, diff_text, language))
    return diff_id

def insert_generated_message(prompt_id, diff_id, model, generated_output, response_time):
    """
    Generates a UUID and stores a generated message in the GeneratedMessages table.
    """
    message_id = str(uuid.uuid4())
    db.execute("INSERT INTO GeneratedMessages (message_id, prompt_id, diff_id, model, generated_output, response_time) VALUES (?, ?, ?, ?, ?, ?, ?)",
               (message_id, prompt_id, diff_id, model, generated_output, response_time))
    return message_id