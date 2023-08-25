from http import HTTPStatus

from fastapi.testclient import TestClient


def test_basic_stuff(test_client: TestClient) -> None:
    res = test_client.get("/stuff", headers={"Authorization": "Bearer abcd"})
    assert res.status_code == HTTPStatus.OK
