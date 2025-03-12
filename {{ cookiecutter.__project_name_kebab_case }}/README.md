# {{ cookiecutter.__project_name_kebab_case }}

{{ cookiecutter.app_description }}

## Using

## Contributing

<details>
<summary>Developing</summary>
{% if cookiecutter.with_conventional_commits|int %}
- This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen).
{%- endif %}
- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `poetry add {package}` from within the development environment to install a run time dependency and add it to `pyproject.toml` and `poetry.lock`. Add `--group test` or `--group dev` to install a CI or development dependency, respectively.
- Run `poetry update` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`.
{%- if cookiecutter.with_conventional_commits|int %}
- Run `cz bump` to bump the app's version, update the `CHANGELOG.md`, and create a git tag.
{%- endif %}

</details>

## Researchers

This project is conducted by:

- **Project Lead:** {{ cookiecutter.app_lead_name }}
- **Other Authors:** {{ cookiecutter.researchers_names }}

For more details or to track progress, visit the [OpenProject board]({{ cookiecutter.openproject_url }}).
