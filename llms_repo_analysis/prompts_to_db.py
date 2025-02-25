


import uuid
import duckdb
from src.logging_metrics import insert_prompt

db = duckdb.connect("llm_analysis.db")

def insert_prompt(prompt_text, metric):
    """
    Generates a UUID and stores the prompt in the Prompts table.
    """
    prompt_id = str(uuid.uuid4())
    db.execute("INSERT INTO Prompts (prompt_id, prompt_text, metric) VALUES (?, ?, ?)", (prompt_id, prompt_text, metric))
    return prompt_id

diffs_placeholder = "{diffs}"
commit_messages_placeholder = "{commit_messages}"

prompt1 = (
    "You are an expert code reviewer. Analyze the provided code changes and evaluate their quality. "
    "Provide constructive feedback on whether the code is well-structured, follows best practices, "
    "is efficient, and maintains readability. Identify potential issues such as bad patterns, security risks, "
    "or performance bottlenecks. Summarize your review in clear bullet points.\n\n"
    "### File Diffs:\n" + diffs_placeholder
)

prompt2 = (
    "You are an expert at writing professional and concise Pull Request descriptions following best practices. "
    "Analyze the provided commit messages and file changes to generate a clear and informative summary. "
    "Follow conventional commit guidelines such as 'fix:', 'feat:', 'chore:', etc. to categorize the changes. "
    "The output should be in bullet points, focusing only on the most relevant modifications.\n\n"
    "### Commit Messages:\n" + commit_messages_placeholder + "\n\n"
    "### File Diffs:\n" + diffs_placeholder
)

# Prompts in die Datenbank einfügen
print(insert_prompt(prompt1, "code_review"))
print(insert_prompt(prompt2, "pull_request_description"))