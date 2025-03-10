import os
import shutil

# Read Cookiecutter configuration.
project_name = "{{ cookiecutter.__project_name_snake_case }}"
development_environment = "{{ cookiecutter.development_environment }}"
with_fastapi_api = int("{{ cookiecutter.with_fastapi_api }}")
with_typer_cli = int("{{ cookiecutter.with_typer_cli }}")
continuous_integration = "{{ cookiecutter.continuous_integration }}"
include_speech= int("{{ cookiecutter.include_speech }}")
with_streamlit = int("{{ cookiecutter.with_streamlit }}")

# Remove py.typed and Dependabot if not in strict mode.
if development_environment != "strict":
    os.remove(f"src/{project_name}/py.typed")
    os.remove(".github/dependabot.yml")

# Remove FastAPI if not selected.
if not with_fastapi_api:
    os.remove(f"src/{project_name}/api.py")
    os.remove("tests/test_api.py")

# Remove Typer if not selected.
if not with_typer_cli:
    os.remove(f"src/{project_name}/cli.py")
    os.remove("tests/test_cli.py")

# Remove the continuous integration provider that is not selected.
if continuous_integration != "GitHub":
    shutil.rmtree(".github/")
elif continuous_integration != "GitLab":
    os.remove(".gitlab-ci.yml")

# Remove unused GitHub Actions workflows.
if continuous_integration == "GitHub":
    if os.path.exists(".github/workflows/publish.yml"):
        os.remove(".github/workflows/publish.yml")

if not include_speech:
    os.remove(f"src/{project_name}/speech.py")

if not with_streamlit:
    os.remove("app.py")
    shutil.rmtree(".streamlit/")