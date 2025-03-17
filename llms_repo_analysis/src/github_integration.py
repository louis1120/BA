import os
import typer
from github import Github, GithubException

def get_github_instance():
    """
    Returns an authenticated GitHub client instance.
    Reads tokens from environment variables.
    """
      github_token = os.getenv('GITHUB_TOKEN')
      
      if not github_token:
          raise EnvironmentError("Missing Public GitHub authentication token in environment variables.")
      
      try:
          client = Github(login_or_token=github_token, timeout=600)
          return client
      except GithubException as e:
          raise ValueError(f"Failed to authenticate with Public GitHub: {e}")
