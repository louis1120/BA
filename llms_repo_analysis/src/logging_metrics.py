import uuid
import duckdb

def insert_code_diff(diff_text: str, commit_messages: str, repository: str, pr_number: int) -> uuid.UUID:
    db = duckdb.connect("llm_analysis.db")
    
    # Generate UUID for the new entry
    pr_id = uuid.uuid4()

    # Insert into CodeDiffs table
    db.execute("""
    INSERT INTO CodeDiffs (pr_id, diff_text, commit_messages, repository, pr_number)
    VALUES (?, ?, ?, ?, ?)
    """, (pr_id, diff_text, commit_messages, repository, pr_number))
    
    # Fetch and print the inserted data
    inserted_data = db.execute("SELECT * FROM CodeDiffs WHERE pr_id = ?", (pr_id,)).fetchall()
    db.close()
    
    print(f"CodeDiff erfolgreich eingefügt! 🚀 PR ID: {pr_id}")
    print("Eingefügte Daten:", inserted_data)
    return pr_id

def insert_generated_message(prompt_id: uuid.UUID, pr_id: uuid.UUID, model: str, generated_output: str, response_time: float) -> uuid.UUID:
    db = duckdb.connect("llm_analysis.db")
    
    # Generate UUID for the new entry
    message_id = uuid.uuid4()
    
    # Insert into GeneratedMessages table
    db.execute("""
    INSERT INTO GeneratedMessages (message_id, prompt_id, pr_id, model, generated_output, response_time)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (message_id, prompt_id, pr_id, model, generated_output, response_time))
    
    # Fetch and print the inserted data
    inserted_data = db.execute("SELECT * FROM GeneratedMessages WHERE message_id = ?", (message_id,)).fetchall()
    db.close()
    
    print(f"GeneratedMessage erfolgreich eingefügt! 🚀 Message ID: {message_id}")
    print("Eingefügte Daten:", inserted_data)

def insert_evaluation(message_id: uuid.UUID, evaluation_method: str, answer_relevancy: float, hallucination_rate: float, prompt_alignment: float) -> uuid.UUID:
    db = duckdb.connect("llm_analysis.db")
    
    # Generate UUID for the new entry
    evaluation_id = uuid.uuid4()
    
    # Insert into Evaluations table
    db.execute("""
    INSERT INTO Evaluations (evaluation_id, message_id, evaluation_method, answer_relevancy, hallucination_rate, prompt_alignment)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (evaluation_id, message_id, evaluation_method, answer_relevancy, hallucination_rate, prompt_alignment))
    
    # Fetch and print the inserted data
    inserted_data = db.execute("SELECT * FROM Evaluations WHERE evaluation_id = ?", (evaluation_id,)).fetchall()
    db.close()
    
    print(f"Evaluation erfolgreich eingefügt! 🚀 Evaluation ID: {evaluation_id}")
    print("Eingefügte Daten:", inserted_data)
    return evaluation_id
