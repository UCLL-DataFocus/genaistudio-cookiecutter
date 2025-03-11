import os
from pathlib import Path
from github import Github
from github.GithubException import GithubException

def get_github_token():
    """Get GitHub token from the user's home directory."""
    token_path = Path.home() / '.github' / 'token'
    if not token_path.exists():
        raise FileNotFoundError(
            "GitHub token not found. Please create ~/.github/token with your GitHub token"
        )
    return token_path.read_text().strip()

def create_github_repository(repo_name: str, description: str) -> str:
    """
    Create a new GitHub repository.
    
    Parameters
    ----------
    repo_name : str
        Name of the repository
    description : str
        Repository description
    
    Returns
    -------
    str
        Clone URL of the created repository
    """
    try:
        g = Github(get_github_token())
        user = g.get_user()
        repo = user.create_repo(
            name=repo_name,
            description=description,
            private=True,
            has_issues=True,
            has_wiki=True,
            has_downloads=True
        )
        return repo.clone_url
    except GithubException as e:
        print(f"Failed to create repository: {e}")
        return None
