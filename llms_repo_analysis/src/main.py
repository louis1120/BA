from typing import Annotated
from github_integration import get_github_instance
from create_duckdb import create_duckdb
from ai_models import REGISTERED_MODELS
from prompts_to_db import write_prompts_to_db
from utils import  load_prompts, select_models, select_prompt_option
from analysis import pr_analysis
import typer

app = typer.Typer()

def perform_analysis(pr_number: int, repo: str, enterprise: bool, metric: str = "pull_request_description"):
    prompts = load_prompts(metric)
    prompt_id = select_prompt_option(prompts)
    
    g = get_github_instance(enterprise)
    repo = g.get_repo(repo)

    models = select_models()
    for model in models:
        typer.echo(pr_analysis(pr_number, prompt_id, repo, model))

def perform_measurement(pr_number, repo, enterprise, metric):
    prompts = load_prompts(metric)
    g = get_github_instance(enterprise)
    repo = g.get_repo(repo)
    for prompt_id in prompts.keys():
        print(prompt_id)
        for model in REGISTERED_MODELS:
            print(model)
            typer.echo(pr_analysis(pr_number, prompt_id, repo, model))


@app.command()
def generate_pr_description(
    pr_number: Annotated[int, typer.Option("--pullrequest", "-pr")],
    repo: Annotated[str, typer.Option("--repo", "-r")],
    enterprise: Annotated[bool, typer.Option("--enterprise", "-e")] = False
):
    """
    Generate a pull request description.

    Args:
        pr_number (int): The pull request number to which the code review comments will be added.
        repo (str): The repository in the format "owner/repo".
        enterprise (bool): Flag to indicate if the repository is an enterprise repository. Default is False.
    """
    metric = "pull_request_description"
    perform_measurement(pr_number, repo, enterprise, metric)    
        
@app.command()
def interactive_perform_analysis(
    pr_number: Annotated[int, typer.Option("--pullrequest", "-pr")],
    repo: Annotated[str, typer.Option("--repo", "-r")],
    enterprise: Annotated[bool, typer.Option("--enterprise", "-e")] = False
):
    """
    Command to add code review comments to a specified pull request.

    Args:
        pr_number (int): The pull request number to which the code review comments will be added.
        repo (str): The repository in the format "owner/repo".
        enterprise (bool): Flag to indicate if the repository is an enterprise repository. Default is False.
    """
    metric = "pull_request_description"
    perform_analysis(pr_number, repo, enterprise, metric)
    
@app.command()
def create_db():
    """
    Command to generate the DuckDB.
    """
    typer.echo("Generating DuckDB...")
    create_duckdb()
    write_prompts_to_db()

if __name__ == "__main__":
    app()
    
