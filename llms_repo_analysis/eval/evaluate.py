import subprocess
import typer
from data_handler import fetch_all_eval_data_for_deepeval, get_prompt, insert_evaluation
from utils import clean_generated_output
from metrics import evaluate_deepeval
from model import OllamaDeepEval

app = typer.Typer()

@app.command()
def humanfeedback():
    """
    Command to evaluate metrics with human feedback manually.
    """
    typer.echo("Starting Streamlit application...")
    result = subprocess.run(["streamlit", "run", "streamlit_app.py", "--server.port", "8501"])
    typer.echo(result.stdout)
    if result.stderr:
        typer.echo(result.stderr)

@app.command()
def deepeval():
    """
    Command to evaluate metrics with deepeval.
    """
    eval_model_name = "mistral:latest"
    eval_model = OllamaDeepEval(model_name=eval_model_name)

    while True:
        data = fetch_all_eval_data_for_deepeval()

        if not data:
            typer.echo("No more unevaluated messages found. Exiting...")
            break

        message_id, prompt_id, generated_output, model, commit_messages_and_diffs = data

        cleaned_output = clean_generated_output(generated_output)
        prompt = get_prompt(prompt_id)

        evaluation_method, answer_relevancy, faithfulness_score, prompt_alignment = evaluate_deepeval(
            prompt, cleaned_output, eval_model, model, commit_messages_and_diffs
        )

        insert_evaluation(message_id, evaluation_method, answer_relevancy, faithfulness_score, prompt_alignment, eval_model_name)
        typer.echo(f"Evaluated message {message_id} using {eval_model_name}")

@app.command()
def test():
    """
    Run test cases for evaluation.
    """
    eval_model_name = "mistral:latest"  # Ollama model name
    eval_model = OllamaDeepEval(model_name=eval_model_name)  # Instantiate Ollama model

    test_cases = [
        {
            "input_text": "Implement a new multi-factor authentication (MFA) system for improved security.",
            "actual_output": """
            feat: Introduce multi-factor authentication (MFA)

            - Implemented MFA using time-based one-time passwords (TOTP).
            - Integrated with Google Authenticator and Authy.
            - Updated user settings page to enable MFA configuration.
            - Improved security by requiring MFA during sensitive operations.
            """,
            "metric": "pull_request_description",
            "context": "Security enhancement by implementing MFA."
        },
        {
            "input_text": "Describe the recent performance improvements in the application.",
            "actual_output": "The application now supports dark mode and a new sidebar UI.",
            "metric": "pull_request_description",
            "context": "Performance optimization included query caching and lazy loading."
        }
    ]

    for i, test_case in enumerate(test_cases, start=1):
        typer.echo(f"Running test case {i}...")
        result = evaluate_deepeval(
            test_case["input_text"],
            test_case["actual_output"],
            eval_model,
            test_case["metric"],
            test_case["context"]
        )
        typer.echo(f"Test case {i} results: {result}\n")

@app.command()
def report():
    """
    Command to generate a report.
    """
    typer.echo("Generating report...")
    
    print(fetch_all_eval_data_for_deepeval())

if __name__ == "__main__":
    app()

    