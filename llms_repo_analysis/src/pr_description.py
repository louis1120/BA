from ai_models import get_ai_model
from github.PullRequest import PullRequest
from github.Commit import Commit

import duckdb
import uuid
from typing import Tuple, Any

def gen_pr_description(pr: Any, prompt_id: uuid.UUID, model_name: str = "qwen2.5-coder:14B") -> Tuple[str, str]:
    """
    Generates a concise and professional description of a Pull Request based on changed files and commit details.
    """
    try:
        # Verbindung zur DuckDB-Datenbank herstellen
        db = duckdb.connect("llm_analysis.db")
        
        # Prompt aus der Datenbank abrufen
        result = db.execute("SELECT prompt_text FROM Prompts WHERE prompt_id = ?", (prompt_id,)).fetchone()
        if result is None:
            return "Error: Prompt ID not found in the database", ""
        
        prompt_template = result[0]
        
        # Extract diffs from the PR
        diffs = []
        for file in pr.get_files():
            diffs.append(f"File: {file.filename}\nDiff:\n{file.patch}")
        
        # Extract commit messages
        commit_messages = []
        for commit in pr.get_commits():
            commit_messages.append(commit.commit.message)
        
        # Construct the final prompt using the template
        prompt = prompt_template.format(
            commit_messages="\n".join(commit_messages),
            diffs="\n\n".join(diffs)
        )
        
        # Fetch AI model and generate PR description
        model = get_ai_model(model_name)
        response = model.generate_response(prompt)
        
        return response, prompt
    
    except Exception as e:
        return f"Error generating PR description: {e}", ""

