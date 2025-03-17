from typing import Dict
import uuid
from InquirerPy import inquirer
import duckdb
from github.PullRequest import PullRequest
from ai_models import REGISTERED_MODELS
from typing import Tuple



def select_models():
    """
    Prompts the user to select multiple models from a list
    """
    selected_models = inquirer.fuzzy(
        message="Please select the desired model(s) (use SPACE to select)",
        choices=[{"name": model, "value": model} for model in REGISTERED_MODELS],
        multiselect=True,
        default="",
        marker_pl=" [ ] ",
        marker=" [x] ",
        keybindings={
            "toggle": [
                {"key": "space"},
            ],
            "toggle-all-true": [
                {"key": "c-a"},
            ],
            "toggle-all-false": [
                {"key": "c-n"},
            ],
        }
    ).execute()

    return selected_models

def load_prompts(metric: str):
    """
    Load prompts from a DuckDB table based on the specified metric.
    """
    conn = duckdb.connect("llm_analysis.db")
    query = "SELECT prompt_id, prompt_text FROM Prompts WHERE metric = ?"
    result = conn.execute(query, (metric,)).fetchall()
    conn.close()
    return {row[0]: row[1] for row in result}

def select_prompt_option(prompts: Dict[int, str]) -> uuid:
    """
    Prompt the user to select a prompt from the available options using a fuzzy search.
    """
    choices = [{"name": prompt_text[:50] + "...", "value": prompt_id} for prompt_id, prompt_text in prompts.items()]

    selected_prompt_id = inquirer.fuzzy(
        message="Please select the desired prompt",
        choices=choices,
        multiselect=False,
        default="",
        marker_pl=" [ ] ",
        marker=" [x] ",
        keybindings={
            "toggle": [
                {"key": "space"},
            ]
        }
    ).execute()
    
    return selected_prompt_id if selected_prompt_id else "No prompt selected"

def fetch_prompt_and_diffs(pr: PullRequest, prompt_id: uuid.UUID) -> Tuple[str, str, str]:
    """
    Fetches the prompt from the database and extracts diffs and commit messages from the PR.
    """
    db = duckdb.connect("llm_analysis.db")
    
    result = db.execute("SELECT prompt_text FROM Prompts WHERE prompt_id = ?", (prompt_id,)).fetchone()
    if result is None:
        raise ValueError("Prompt ID not found in the database")
    
    prompt = result[0]
    
    diffs = []
    for file in pr.get_files():
        diffs.append(f"File: {file.filename}\nDiff:\n{file.patch}")
    
    commit_messages = []
    for commit in pr.get_commits():
        commit_messages.append(commit.commit.message)
    
    return prompt, "\n\n".join(diffs), "\n".join(commit_messages)
        
