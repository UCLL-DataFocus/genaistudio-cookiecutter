"""Test {{ cookiecutter.__project_name_kebab_case }} REST API."""

import httpx
from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)


def test_read_root() -> None:
    """Test that reading the root is successful."""
    response = client.get("/compute", params={"n": 7})
    assert httpx.codes.is_success(response.status_code)
