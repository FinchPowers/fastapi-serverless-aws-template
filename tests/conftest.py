import pytest
from fastapi.testclient import TestClient

from src.handler import app


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    return TestClient(app)
