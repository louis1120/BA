import uuid 
import duckdb
import typer

def write_prompts_to_db():
    db = duckdb.connect("llm_analysis.db")

    def insert_prompt(prompt_text, metric):
        """
        Generates a UUID and stores the prompt in the Prompts table.
        """
        prompt_id = str(uuid.uuid4())
        db.execute("INSERT INTO Prompts (prompt_id, prompt_text, metric) VALUES (?, ?, ?)", (prompt_id, prompt_text, metric))
        return prompt_id

    few_shot_prompt = """Generate a well-structured and concise Pull Request (PR) description based on the provided commit messages and code changes. 
    Each change should be described in a single short sentence and follow the Conventional Commit Types (feat, fix, chore, refactor, docs, test, etc.). Keep it brief and precise.

    ### Examples of PR Descriptions:

    ---
    Example 1:
    - **chore:** Simplified logic for splitting operations.
    - **chore:** Improved boolean evaluation for readability.
    - **feat:** Enabled global issue collection in config.
    - **chore:** Reformatted code for consistency.

    ---
    Example 2:
    - **fix:** Allowed config generator to accept multiple commands.
    - **fix:** Removed empty PR fields from YAML output.

    ---

    Now, generate a concise PR description for the current Pull Request.

    **Commit Messages:**  
    {commit_messages}

    **Code Changes:**  
    {code_diffs}
    """

    structured_cot_prompt = """You are an experienced software engineer crafting a precise, structured, and concise Pull Request (PR) description. 
    Use a **structured chain-of-thought** approach to ensure clarity. Keep the description short and to the point.

    ### Step 1: Analyze the Changes
    - Read commit messages and code diffs.
    - Identify the purpose of each change.
    - Assign the correct **Conventional Commit Type** (feat, fix, chore, refactor, docs, test, etc.).

    ### Step 2: Structure the PR Description
    - Each change should be in a separate sentence.
    - Start each sentence with the commit type and keep it concise.

    ---
    **Commit Messages:**  
    {commit_messages}

    **Code Changes:**  
    {code_diffs}

    ---

    Now, generate the PR description in the following concise format:

    - **chore:** Simplified logic for splitting operations.
    - **chore:** Improved boolean evaluation for readability.
    - **feat(config):** Enabled global issue collection.
    - **fix:** Allowed config generator to accept multiple commands.
    - **fix:** Removed empty PR fields from YAML output.
    """

    combined_prompt = """Generate a concise and structured Pull Request (PR) description based on the given commit messages and code changes. 
    Each change should be a short sentence, following the Conventional Commit types (feat, fix, chore, refactor, docs, test, etc.). Keep it brief and precise.

    ### Instructions:
    1. Read commit messages and code diffs.
    2. Identify the purpose of each change.
    3. Assign the correct **Conventional Commit Type**.
    4. Format each change as a bullet point in a short and clear sentence.

    ### Example PR Descriptions:

    ---
    #### Example 1:
    - **chore:** Simplified logic for splitting operations.
    - **chore:** Improved boolean evaluation for readability.
    - **feat(config):** Enabled global issue collection.
    - **chore:** Reformatted code for consistency.

    ---
    #### Example 2:
    - **fix:** Allowed config generator to accept multiple commands.
    - **fix:** Removed empty PR fields from YAML output.

    ---

    Now, generate a structured and concise PR description:

    **Commit Messages:**  
    {commit_messages}

    **Code Changes:**  
    {code_diffs}

    ---

    **Expected Output Format:**
    - **{commit_type}:** {Short description of the change}.
    - **{commit_type}:** {Short description of the change}.
    """
    
    typer.echo(insert_prompt(few_shot_prompt, "pull_request_description"))
    typer.echo(insert_prompt(structured_cot_prompt, "pull_request_description"))
    typer.echo(insert_prompt(combined_prompt, "pull_request_description"))