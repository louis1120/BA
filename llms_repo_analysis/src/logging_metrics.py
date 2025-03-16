import uuid
import duckdb

def insert_code_diff(diff_text: str, commit_messages: str, repository: str, pr_number: int) -> uuid.UUID:
    """
    Inserts a new code difference entry into the CodeDiffs table.

    Args:
        diff_text (str): The code difference (diff).
        commit_messages (str): Associated commit messages.
        repository (str): The repository name.
        pr_number (int): The pull request number.

    Returns:
        uuid.UUID: The generated PR ID for the inserted record.
    """
    db = duckdb.connect("llm_analysis.db")

    # Generate a unique PR ID
    pr_id = uuid.uuid4()

    # Insert into CodeDiffs table
    db.execute("""
        INSERT INTO CodeDiffs (pr_id, diff_text, commit_messages, repository, pr_number)
        VALUES (?, ?, ?, ?, ?)
    """, (pr_id, diff_text, commit_messages, repository, pr_number))

    # Fetch and print the inserted data
    db.execute("SELECT * FROM CodeDiffs WHERE pr_id = ?", (pr_id,)).fetchall()
    db.close()
    
    return pr_id

def insert_generated_message(prompt_id: uuid.UUID, pr_id: uuid.UUID, model: str, generated_output: str, total_duration: float, load_duration: float, prompt_tokens: int, prompt_eval_time: float, generated_tokens: int, generation_time: float) -> uuid.UUID:
    """
    Inserts a new generated message entry into the GeneratedMessages table.

    Args:
        prompt_id (uuid.UUID): The ID of the prompt that triggered the generation.
        pr_id (uuid.UUID): The associated PR ID.
        model (str): The model used for generation.
        generated_output (str): The generated response text.
        total_duration (float): Total processing duration.
        load_duration (float): Load duration of the model.
        prompt_tokens (int): Number of prompt tokens.
        prompt_eval_time (float): Evaluation time of the prompt.
        generated_tokens (int): Number of generated tokens.
        generation_time (float): Time taken for text generation.

    Returns:
        uuid.UUID: The generated message ID for the inserted record.
    """
    db = duckdb.connect("llm_analysis.db")

    # Generate a unique message ID
    message_id = uuid.uuid4()

    # Insert into GeneratedMessages table
    db.execute("""
        INSERT INTO GeneratedMessages (message_id, prompt_id, pr_id, model, generated_output, total_duration, load_duration, prompt_tokens, prompt_eval_time, generated_tokens, generation_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (message_id, prompt_id, pr_id, model, generated_output, total_duration, load_duration, prompt_tokens, prompt_eval_time, generated_tokens, generation_time))

    # Fetch and print the inserted data
    inserted_data = db.execute("SELECT * FROM GeneratedMessages WHERE message_id = ?", (message_id,)).fetchall()
    db.close()

    print(f"GeneratedMessage successfully inserted! 🚀 Message ID: {message_id}")
    print("Inserted Data:", inserted_data)
