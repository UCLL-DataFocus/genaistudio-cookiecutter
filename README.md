# 🍪 GenAI Studio Cookiecutter

A modern [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating Poetry Python web apps for GenAI Studio (GPT Academy).

## 🎁 Features

- 🌈 Cross-platform support for Linux, macOS (Apple silicon and Intel), and Windows 
- 📦 Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
- ⚡️ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
- ✍️ Code formatting with [Ruff](https://github.com/charliermarsh/ruff)
- ✅ Code linting with [Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy), and [Ruff](https://github.com/charliermarsh/ruff)
- 🏷 Optionally follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen) ?
- 💌 Verified commits with [GPG](https://gnupg.org/) ?
- 🧪 Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
- 🏗 Scaffolding updates with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://github.com/cruft/cruft)
- 🧰 Dependency updates with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)

## ✨ Using

### Creating a new Python project

To create a new Python project with this template:

1. Install the latest [Cruft](https://github.com/cruft/cruft) and [Cookiecutter](https://github.com/cookiecutter/cookiecutter) in your [Python environment](https://github.com/pyenv/pyenv-virtualenv) with:

   ```sh
   pip install --upgrade "cruft>=2.12.0" "cookiecutter>=2.1.1"
   ```

2. In the directory where you want to create your new repository, run the following command to apply the Poetry Cookiecutter template:

   ```sh
   cruft create -f https://github.com/UCLL-DataFocus/genaistudio-cookiecutter
   ```

### Optional: Automatic GitHub Repository Creation

If you'd like the cookiecutter to automatically initialize Git, create a GitHub repository, and push your initial commit, set the `first_time_creation` parameter to `"1"`. **Important:** For this feature to work, ensure you have your GitHub personal access token stored in a file at `~/.github/token` in your home directory.

### Updating your Python project

To update your Python project to the latest template version:

1. Update the project while verifying the existing template parameters and setting any new parameters, if there are any:

   ```sh
   cruft update --cookiecutter-input
   ```

2. If any of the file updates failed, resolve them by inspecting the corresponding `.rej` files.

## 🤓 Template parameters

| Parameter                                                                 | Description                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PWO_acroniem` <br> "genaistudio"              | 	A short acronym for your project (e.g., genaistudio). This prefix is automatically added to the project name.                                                                                                                               |
| `app_name` <br> "chatbot"                                  | The name of your application. The PWO acronym is automatically added to create a unique project name.                                                                                                                               |
| `openproject_url` <br> "https://ucll.openproject.com/projects/genai-studio/"   | The URL to your project's management page or repository.                                                                                                                                                                                                                                                                                             |
| `app_description` <br> "A Python app that reticulates splines."         | A brief, one-line description of your app's purpose.repository.                                                                                                                                                                                                                                                                                                  |
| `app_lead_name` <br> "John Smith"                                           | The full name of the primary author of the app.                                                                                                                                                                                                                                                                                   |
| `researchers_names` <br> "Bob Johnson, Alice Brown, Charlie White"                                | A comma-separated list of names for the researchers or contributors.                                                                                                                                                                                                                                                                             |
| `python_version` <br> "3.10.9"                                              | The minimum required Python version for the project.                                                                                                                                                                                                                                                                                 |
| `with_streamlit` <br> ["0", "1"]                                   | Set to "1" to include Streamlit support (for interactive web UI) or "0" to exclude it.                                                                                                                                                                                                                                                                             |
| `include_speech` <br> ["0", "1"]                                         | Set to "1" to include speech recognition functionality; "0" to exclude it.                                                                                                                                                                                                                                                                         |
| `include_notebooks` <br> ["0", "1"]                                           | Set to "1" to include example notebooks; "0" to exclude them.                                                                                                                                                                                                                                                                         |
| `work_with_data` <br> ["0", "1"]                                             | Set to "1" if your project will handle data operations; "0" otherwise.                                                                                                                                                                                                                                                                            |
| `development_environment` <br> ["simple", "strict"]                       | Whether to configure the development environment with a focus on simplicity or with a focus on strictness. In strict mode, additional [Ruff rules](https://docs.astral.sh/ruff/rules/) are added, and tools such as [Mypy](https://github.com/python/mypy) and [Pytest](https://github.com/pytest-dev/pytest) are set to strict mode. |
| `with_conventional_commits` <br> ["0", "1"]                               | If "1", [Commitizen](https://github.com/commitizen-tools/commitizen) will verify that your commits follow the [Conventional Commits](https://www.conventionalcommits.org/) standard. In return, `cz bump` may be used to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/).     |
| `with_fastapi_api` <br> ["0", "1"]                                        | If "1", [FastAPI](https://github.com/tiangolo/fastapi) is added as a run time dependency, FastAPI API stubs and tests are added, a `poe api` command for serving the API is added.                                                                                                                                                    |
| `with_typer_cli` <br> ["0", "1"]                                          | If "1", [Typer](https://github.com/tiangolo/typer) is added as a run time dependency, Typer CLI stubs and tests are added, the package itself is registered as a CLI.                                                                                                                                                                 |
| `continuous_integration` <br> ["GitHub", "GitLab"]                        | Whether to include a [GitHub Actions](https://docs.github.com/en/actions) or a [GitLab CI/CD](https://docs.gitlab.com/ee/ci/) continuous integration workflow for testing the project, and publishing the package or deploying the app.                                                                                               |
| `github_repo_name` <br> "genaistudio-chatbot"                                             | Defaults to "PWO_acroniem"-"app_name" and is used as the GitHub repository name.                                                                                                                                                                                                                                                                                      |
| `first_time_creation` <br> ["0", "1"]                                          | Set to "1" to automatically initialize Git, create a GitHub repository using your .github/token, and push the initial commit; set to "0" to skip these steps.                                                                                                                                                                                                                                                                                     |