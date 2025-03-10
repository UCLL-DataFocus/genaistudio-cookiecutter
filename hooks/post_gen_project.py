import os
import shutil

# Read Cookiecutter configuration.
development_environment = "{{ cookiecutter.development_environment }}"
with_fastapi_api = int("{{ cookiecutter.with_fastapi_api }}")
with_typer_cli = int("{{ cookiecutter.with_typer_cli }}")
include_speech= int("{{ cookiecutter.include_speech }}")
with_streamlit = int("{{ cookiecutter.with_streamlit }}")

# Remove py.typed and Dependabot if not in strict mode.
if development_environment != "strict":
    os.remove(f"src/py.typed")
    os.remove(".github/dependabot.yml")

# Remove FastAPI if not selected.
if not with_fastapi_api:
    os.remove(f"src/api.py")
    os.remove("tests/test_api.py")

# Remove Typer if not selected.
if not with_typer_cli:
    os.remove(f"src/cli.py")
    os.remove("tests/test_cli.py")

if not include_speech:
    os.remove(f"src/speech.py")

if not with_streamlit:
    os.remove("app.py")
    shutil.rmtree(".streamlit/")