import uuid
import duckdb


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

def fetch_all_eval_data_for_deepeval():
    db = duckdb.connect("llm_analysis.db")
    
    query = """
    SELECT gm.message_id, gm.prompt_id, gm.generated_output, gm.model, cd.pr_id
    FROM GeneratedMessages gm
    LEFT JOIN Evaluations e ON gm.message_id = e.message_id
    JOIN CodeDiffs cd ON gm.pr_id = cd.pr_id
    WHERE e.message_id IS NULL
    LIMIT 1;
    """
    
    result = db.execute(query).fetchone()
    db.close()

    if not result:
        return None

    message_id, prompt_id, generated_output, model, pr_id = result

    commit_messages_and_diffs = get_commit_messages_and_diffs_by_pr_id(pr_id)

    return message_id, prompt_id, generated_output, model, commit_messages_and_diffs

    
def get_prompt(prompt_id):
    db = duckdb.connect("llm_analysis.db")
    query = """
    SELECT prompt_text 
    FROM Prompts 
    WHERE prompt_id = ?
    """
    
    result = db.execute(query, [prompt_id]).fetchone()
    
    if result:
        return result
    else:
        return None
    
def get_commit_messages_and_diffs_by_pr_id(pr_id: str):
    """
    Retrieves commit messages and code diffs for a given PR ID.

    :param pr_id: The UUID of the PR to retrieve commit messages and diffs for.
    :return: A list containing commit messages and code diffs as strings.
    """
    db = duckdb.connect("llm_analysis.db")

    # Query to fetch commit messages and code diffs for the given PR ID
    query = f"""
    SELECT commit_messages, diff_text FROM CodeDiffs
    WHERE pr_id = '{pr_id}';
    """
    
    results = db.execute(query).fetchall()
    db.close()

    if not results:
        print(f"⚠️ No data found for PR ID: {pr_id}")
        return []

    # Extract the first row (assuming there's only one entry per PR ID)
    commit_messages, code_diff = results[0]

    # Convert None values to empty strings if necessary
    commit_messages = commit_messages if commit_messages else ""
    code_diff = code_diff if code_diff else ""

    return [commit_messages, code_diff]