from http import HTTPStatus

from fastapi.testclient import TestClient


def test_basic_router_token(test_client: TestClient) -> None:
    result = test_client.get("/token")
    assert result.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
