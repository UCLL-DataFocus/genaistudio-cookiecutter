import os
import sys
import shutil
import subprocess
import requests

# Read Cookiecutter configuration
development_environment = "{{ cookiecutter.development_environment }}"
with_fastapi_api = int("{{ cookiecutter.with_fastapi_api }}")
with_typer_cli = int("{{ cookiecutter.with_typer_cli }}")
include_speech = int("{{ cookiecutter.include_speech }}")
with_streamlit = int("{{ cookiecutter.with_streamlit }}")
first_time_creation = int("{{ cookiecutter.first_time_creation }}")
repo_name = "{{ cookiecutter.github_repo_name }}"
repo_description = "{{ cookiecutter.app_description }}"
include_llm = int("{{ cookiecutter.include_llm }}")

# ✅ Step 1: Remove unneeded files based on user selections
if development_environment != "strict":
    os.remove("src/py.typed")
    os.remove(".github/dependabot.yml")

if not with_fastapi_api:
    os.remove("src/api.py")
    os.remove("tests/test_api.py")

if not with_typer_cli:
    os.remove("src/cli.py")
    os.remove("tests/test_cli.py")

if not include_speech:
    os.remove("src/speech.py")

if not with_streamlit:
    os.remove("app.py")
    shutil.rmtree(".streamlit/")

if not include_llm:
    shutil.rmtree("src/models/")
    shutil.rmtree("src/config/")
    shutil.rmtree("Config/")
    shutil.rmtree("src/components/")

if include_llm:
    llms_string = "{{ cookiecutter["llm's (comma-separated, press Enter for all)"] }}"
    # Split by comma, strip whitespace, then see if "llama3" is included
    llms_list = [llm.strip() for llm in llms_string.split(",")]
    if "llama3" not in llms_list:
        llama3_path = "src/models/custom/llama3.py"
        if os.path.exists(llama3_path):
            os.remove(llama3_path)
    if "mistral-large" not in llms_list:
        mistral_path = "src/models/custom/mistral_large.py"
        if os.path.exists(mistral_path):
            os.remove(mistral_path)
    custom_llms_folder = "src/models/custom"
    if os.path.isdir(custom_llms_folder) and not os.listdir(custom_llms_folder):
        os.rmdir(custom_llms_folder)

# ✅ Step 2: Helper function to run shell commands safely
def run_command(command):
    """Runs a shell command and exits on failure."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ ERROR: Command failed: {command}\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

# ✅ Step 3: Retrieve GitHub token from `~/.github/token`
def get_github_token():
    """Retrieve GitHub token stored in `~/.github/token`."""
    token_path = os.path.expanduser("~/.github/token")

    if not os.path.exists(token_path):
        print("❌ ERROR: GitHub token not found.")
        print("ℹ️  Please create a file at `~/.github/token` with your GitHub personal access token.")
        sys.exit(1)

    return open(token_path, "r").read().strip()

# ✅ Step 4: Create GitHub repository using the API
def create_github_repository(repo_name, description):
    """Create a new GitHub repository using the GitHub API."""
    token = get_github_token()
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    data = {"name": repo_name, "description": description, "private": True}

    print(f"🔄 Creating GitHub repository '{repo_name}'...")
    response = requests.post("https://api.github.com/user/repos", json=data, headers=headers)

    if response.status_code == 201:
        print(f"✅ Repository created: {response.json()['html_url']}")
        return response.json()["clone_url"]
    else:
        print(f"❌ ERROR: Failed to create GitHub repository: {response.json()}")
        sys.exit(1)

# ✅ Step 5: Initialize Git and push the project if `first_time_creation` is enabled
if first_time_creation:
    print("\n🚀 Initializing Git repository...")

    run_command("git init")
    run_command("git add .")
    run_command('git commit -m "Initial commit"')

    print("🔄 Creating GitHub repository...")
    clone_url = create_github_repository(repo_name, repo_description)

    if clone_url:
        print(f"🔗 Adding remote repository: {clone_url}")
        run_command(f"git remote add origin {clone_url}")
        run_command("git branch -M main")
        run_command("git push -u origin main")

        print(f"🎉 Successfully created and pushed to GitHub: {clone_url}")
    else:
        print("⚠️ GitHub repository was not created. You can set it up manually later.")
