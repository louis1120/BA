import re
import duckdb
import typer


def get_all_evaluations():
    db = duckdb.connect("llm_analysis.db")
    evaluations = db.execute("SELECT * FROM Evaluations").fetchall()
    if not evaluations:
        typer.echo("No evaluations found.")
        return
    
    for eval in evaluations:
        typer.echo(f"Evaluation ID: {eval[0]}")
        typer.echo(f"Message ID: {eval[1]}")
        typer.echo(f"Evaluation Method: {eval[2]}")
        typer.echo(f"Evaluation Model: {eval[3]}")
        typer.echo(f"Alignment Score: {eval[4]}")
        typer.echo(f"Relevance Score: {eval[5]}")
        typer.echo(f"Faithfullness: {eval[6]}")
        typer.echo("-" * 40)

def clean_generated_output(output: str) -> str:
    """
    Cleans the generated output by removing everything before and including the last '</think>' tag.
    
    :param output: The generated text output.
    :return: The cleaned generated text.
    """
    # Find the last occurrence of '</think>'
    last_think_end = output.rfind("</think>")
    
    # If '</think>' exists, keep everything after it
    if last_think_end != -1:
        output = output[last_think_end + len("</think>"):].strip()
    
    return output