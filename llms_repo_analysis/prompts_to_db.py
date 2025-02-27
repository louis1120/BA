import uuid
import duckdb
import typer

def write_prompts_to_db():
    db = duckdb.connect("llms_repo_analysis/llm_analysis.db")

    def insert_prompt(prompt_text, metric):
        """
        Generates a UUID and stores the prompt in the Prompts table.
        """
        prompt_id = str(uuid.uuid4())
        db.execute("INSERT INTO Prompts (prompt_id, prompt_text, metric) VALUES (?, ?, ?)", (prompt_id, prompt_text, metric))
        return prompt_id

    prompt1 = (
        "You are an expert code reviewer. Analyze the provided code changes and evaluate their quality. "
        "Provide constructive feedback on whether the code is well-structured, follows best practices, "
        "is efficient, and maintains readability. Identify potential issues such as bad patterns, security risks, "
        "or performance bottlenecks. Summarize your review in clear bullet points.\n\n"
    )

    prompt2 = (
        "You are an expert at writing professional and concise Pull Request descriptions following best practices. "
        "Analyze the provided commit messages and file changes to generate a clear and informative summary. "
        "Follow conventional commit guidelines such as 'fix:', 'feat:', 'chore:', etc. to categorize the changes. "
        "The output should be in bullet points, focusing only on the most relevant modifications.\n\n"
    )

    typer.echo(insert_prompt(prompt1, "code_review"))
    typer.echo(insert_prompt(prompt2, "pull_request_description"))