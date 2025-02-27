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


def insert_generated_message(prompt_id: uuid.UUID, pr_id: uuid.UUID, model: str, generated_output: str, response_time: float) -> uuid.UUID:
    """
    Inserts a new generated message entry into the GeneratedMessages table.

    Args:
        prompt_id (uuid.UUID): The ID of the prompt that triggered the generation.
        pr_id (uuid.UUID): The associated PR ID.
        model (str): The model used for generation.
        generated_output (str): The generated response text.
        response_time (float): The response time of the model.

    Returns:
        uuid.UUID: The generated message ID for the inserted record.
    """
    db = duckdb.connect("llm_analysis.db")

    # Generate a unique message ID
    message_id = uuid.uuid4()

    # Insert into GeneratedMessages table
    db.execute("""
        INSERT INTO GeneratedMessages (message_id, prompt_id, pr_id, model, generated_output, response_time)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (message_id, prompt_id, pr_id, model, generated_output, response_time))

    # Fetch and print the inserted data
    inserted_data = db.execute("SELECT * FROM GeneratedMessages WHERE message_id = ?", (message_id,)).fetchall()
    db.close()

    print(f"GeneratedMessage successfully inserted! 🚀 Message ID: {message_id}")
    print("Inserted Data:", inserted_data)

    return message_id


def insert_evaluation(message_id: uuid.UUID, evaluation_method: str, answer_relevancy: float, faithfulness: float, prompt_alignment: float, evaluation_model: str) -> uuid.UUID:
    """
    Inserts a new evaluation entry into the Evaluations table.

    Args:
        message_id (uuid.UUID): The ID of the evaluated message.
        evaluation_method (str): The method of evaluation (e.g., 'human_feedback' or 'deepeval').
        answer_relevancy (float): The relevancy score of the answer.
        faithfulness (float): The faithfulness score.
        prompt_alignment (float): The prompt alignment score.
        evaluation_model (str): The model used for evaluation.

    Returns:
        uuid.UUID: The generated evaluation ID for the inserted record.
    """
    db = duckdb.connect("llm_analysis.db")

    # Generate a unique evaluation ID
    evaluation_id = uuid.uuid4()

    # Insert into Evaluations table
    db.execute("""
        INSERT INTO Evaluations (evaluation_id, message_id, evaluation_method, evaluation_model, answer_relevancy, faithfulness, prompt_alignment)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (evaluation_id, message_id, evaluation_method, evaluation_model, answer_relevancy, faithfulness, prompt_alignment))

    # Fetch and print the inserted data
    inserted_data = db.execute("SELECT * FROM Evaluations WHERE evaluation_id = ?", (evaluation_id,)).fetchall()
    db.close()

    print(f"Evaluation successfully inserted! 🚀 Evaluation ID: {evaluation_id}")
    print("Inserted Data:", inserted_data)

    return evaluation_id
