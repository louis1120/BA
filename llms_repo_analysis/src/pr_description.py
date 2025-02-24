import typer
from ai_models import get_ai_model
from utils import handle_feedback

def get_prs(repositories, model):
    for repo in repositories:
        typer.echo(repo.full_name)
        pull_requests = repo.get_pulls(state='open', direction='desc')
        typer.echo(f"Number of open pull requests: {len(list(pull_requests))}")
        for pr in pull_requests[:1]:
            response, prompt = gen_pr_description(pr, model)
            while typer.confirm("Do you have any feedback?"):
                handle_feedback(prompt, response, model)
            # pr.changed_files => pass the changed files to the LLM as well

def gen_pr_description(pr, model_name: str = "qwen2.5-coder:14B"):
    """
    Creates a formatted prompt for an LLM to generate a pull request description.

    :param pr: A pull request object from PyGithub
    :param model_name: The name of the AI model to use
    :return: Formatted prompt as a string
    """
    try:
        model = get_ai_model(model_name)
        # PR basic data
        title = pr.title.strip() if pr.title else "No title available"
        pr_description = pr.body.strip() if pr.body else "No PR description available."
        num_commits = pr.commits
        comments = pr.comments
        review_comments = pr.review_comments

        # Fetch PR comments
        issue_comments = [comment.body.strip() for comment in pr.get_issue_comments() if comment.body and comment.body.strip()]
        if not issue_comments:
            issue_comments = ["No general comments available."]

        # Fetch review comments
        review_comments = [review.body.strip() for review in pr.get_reviews() if review.body and review.body.strip()]
        if not review_comments:
            review_comments = ["No review comments available."]

        # Fetch commit diffs
        commit_diffs = []
        for commit in pr.get_commits():
            commit_data = pr.base.repo.get_commit(commit.sha)  # Fetch commit details
            diff_texts = [
                f"File: {file.filename}\n{getattr(file, 'patch', 'No diff available')}"
                for file in commit_data.files
            ]

            if not diff_texts:
                diff_texts = ["No diff available"]

            commit_diffs.append(f"**Commit {commit.sha[:7]}**:\n" + "\n".join(diff_texts) + "\n")

        commit_diff_text = "\n\n".join(commit_diffs) if commit_diffs else "No commit diffs available."

        # Format comments
        formatted_comments = "\n".join(f"- {comment}" for comment in issue_comments)
        formatted_review_comments = "\n".join(f"- {comment}" for comment in review_comments)

        # Create prompt for the LLM
        prompt = f"""
        ### Task:
        You are an experienced software developer and reviewer. Your task is to create a **structured PR description**.
        The description should include a title, a summary of the changes, key changes, and additional context.
        Use the attached information to create a meaningful and informative description according to the guidelines.
        
        ### **Pull Request Details**
        - **Title:** {title}
        - **Description:** {pr_description}
        - **Number of Commits:** {num_commits}
        - **General Comments:** {comments}
        - **Review Comments:** {review_comments}

        ### **Commit Changes (Diffs):**
        {commit_diff_text}

        ### **Comments & Reviews:**
        **General Comments:**
        {formatted_comments}

        **Review Comments:**
        {formatted_review_comments}
        """
        # Generate the response using the AI model
        response = model.generate_response(prompt)
        return response, prompt
    except Exception as e:
        return f"Error generating PR description: {e}"