"""Test {{ cookiecutter.__project_name }}."""

import src


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(src.__name__, str)
