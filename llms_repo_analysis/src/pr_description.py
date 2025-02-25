from ai_models import get_ai_model
from github.PullRequest import PullRequest
from github.Commit import Commit

def gen_pr_description(pr: PullRequest, model_name: str = "qwen2.5-coder:14B"):
    """
    Generates a concise and professional description of a Pull Request based on changed files and commit details.
    """
    try:
        # Extract diffs from the PR
        diffs = []
        for file in pr.get_files():
            diffs.append(f"File: {file.filename}\nDiff:\n{file.patch}")
        
        # Extract commit messages and diffs
        commit_messages = []
        commit_diffs = []
        for commit in pr.get_commits():
            if isinstance(commit, Commit):
                commit_messages.append(commit.commit.message)
                commit_diffs.append(commit.files)
        
        # Construct a structured prompt for the AI model
        prompt = (
            "You are an expert at writing professional and concise Pull Request descriptions following best practices. "
            "Analyze the provided commit messages and file changes to generate a clear and informative summary. "
            "Follow conventional commit guidelines such as 'fix:', 'feat:', 'chore:', etc. to categorize the changes. "
            "The output should be in bullet points, focusing only on the most relevant modifications.\n\n"
            "### Commit Messages:\n" + "\n".join(commit_messages) + "\n\n"
            "### File Diffs:\n" + "\n\n".join(diffs)
        )
        
        # Fetch AI model and generate PR description
        model = get_ai_model(model_name)
        response = model.generate_response(prompt)
        return response, prompt
    
    except Exception as e:
        return f"Error generating PR description: {e}"
    
