from http import HTTPStatus

from src import handler
from src.types import build_ApiGatewayLambdaEvent


def test_mangum_integration() -> None:
    event = build_ApiGatewayLambdaEvent(
        # any route would do for that test
        path="/docs",
        httpMethod="GET",
    )
    res = handler.handler(event=event, context={})  # type: ignore[arg-type]
    assert res["statusCode"] == HTTPStatus.OK
