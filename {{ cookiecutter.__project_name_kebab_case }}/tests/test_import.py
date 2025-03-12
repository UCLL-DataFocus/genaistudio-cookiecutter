"""Test {{ cookiecutter.__project_name_kebab_case }}."""

import src


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(src.__name__, str)
