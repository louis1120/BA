import typer
from utils import handle_feedback


def collect_eval(prompt, generated_output: str, model):
    """
    Interact with the user to check satisfaction, accuracy, and handle feedback.
    """
    while True:
        satisfied = typer.confirm("Are you satisfied with the output?")
        if satisfied:
            accurate = typer.confirm("Is the output accurate?")
            if not accurate:
                typer.echo("Please note that the output might contain hallucinations.")
            rerun_with_feedback = typer.confirm("Do you want to do it again with feedback?")
            if rerun_with_feedback:
                handle_feedback(prompt, generated_output, model)
            else:
                break
        else:
            rerun_with_feedback = typer.confirm("Do you want to do it again with feedback?")
            if rerun_with_feedback:
                handle_feedback(prompt, generated_output, model)
            else:
                break
