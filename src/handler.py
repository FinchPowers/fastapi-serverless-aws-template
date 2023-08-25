from typing import cast

import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from src import runtime_info
from src.routers import stuff, token
from src.types import ApiGatewayLambdaEvent, ApiGatewayLambdaResponse, LambdaContext

root_path = "/v1" if runtime_info.IS_RUNNING_AS_LAMBDA else ""
app = FastAPI(
    root_path=root_path,
    title="fastapi-serverless-aws-template",
    version="dev",
    description="TODO replace description",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=runtime_info.ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stuff.router, prefix="/stuff")
app.include_router(token.router, prefix="/token")

# init_logging()

# _handler and handler are used in the AWS Lambda environment
_handler = Mangum(app, api_gateway_base_path=root_path)
log = structlog.get_logger(__name__)


def handler(event: ApiGatewayLambdaEvent, context: LambdaContext) -> ApiGatewayLambdaResponse:
    return cast(ApiGatewayLambdaResponse, _handler(event, context))  # type: ignore[arg-type]
