from ai_models import get_ai_model
import uuid
from typing import Tuple
from logging_metrics import insert_code_diff, insert_generated_message
from utils import fetch_prompt_and_diffs
from github.Repository import Repository

def pr_analysis(pr_number: int, prompt_id: uuid.UUID, repo: Repository, model_name: str = "qwen2.5-coder:14B") -> Tuple[str, str, float]:
    """
    Generates a concise and professional description of a Pull Request based on changed files and commit details.
    """
    try:
        pr = repo.get_pull(pr_number)
        prompt, diffs, commit_messages = fetch_prompt_and_diffs(pr, prompt_id)
        repository = repo.full_name
        pr_id = insert_code_diff(diffs, commit_messages, repository, pr_number)
        
        context = diffs + commit_messages
        
        # Fetch AI model and generate PR description
        model = get_ai_model(model_name)
        response, total_duration, load_duration, prompt_tokens, prompt_eval_time, generated_tokens, generation_time = model.generate_response(prompt, context)
        message_id = insert_generated_message(prompt_id, pr_id, model.model_name, response, total_duration, load_duration, prompt_tokens, prompt_eval_time, generated_tokens, generation_time)

        return message_id
    
    except Exception as e:
        return f"Error generating PR description: {e}"

