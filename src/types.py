from http import HTTPStatus
from typing import Any, Callable, TypedDict


class ApiGatewayLambdaEventRequestContext(TypedDict):
    resourcePath: str
    httpMethod: str
    path: str


class ApiGatewayLambdaEvent(TypedDict):
    """ApiGatewayLambdaEvent.

    The requestContext element is guaranteed to have the 3 following keys:
    * resourcePath: str
    * httpMethod: str
    * path: str

    Since requestContext can be customized by edge functions and validators, it
    can contain more keys.

    Source: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html#apigateway-example-event
    """

    resource: str
    path: str
    httpMethod: str
    requestContext: ApiGatewayLambdaEventRequestContext  # See Docstring
    headers: dict[str, str]
    multiValueHeaders: dict[str, list[str]]
    queryStringParameters: dict[str, str] | None
    multiValueQueryStringParameters: dict[str, list[str]]
    pathParameters: dict[str, str] | None
    stageVariables: dict[str, str]
    body: Any
    isBase64Encoded: bool


def build_ApiGatewayLambdaEvent(
    *,
    resource: str = "",
    path: str = "",
    httpMethod: str = "",
    requestContext: ApiGatewayLambdaEventRequestContext | None = None,
    headers: dict[str, str] | None = None,
    multiValueHeaders: dict[str, list[str]] | None = None,
    queryStringParameters: dict[str, str] | None = None,
    multiValueQueryStringParameters: dict[str, list[str]] | None = None,
    pathParameters: dict[str, str] | None = None,
    stageVariables: dict[str, str] | None = None,
    body: Any = "",
    isBase64Encoded: bool = False
) -> ApiGatewayLambdaEvent:
    res: ApiGatewayLambdaEvent = {
        "resource": resource,
        "path": path,
        "httpMethod": httpMethod,
        "requestContext": requestContext or {"resourcePath": "", "httpMethod": "", "path": ""},
        "headers": headers or {},
        "multiValueHeaders": multiValueHeaders or {},
        "queryStringParameters": queryStringParameters,
        "multiValueQueryStringParameters": multiValueQueryStringParameters or {},
        "pathParameters": pathParameters,
        "stageVariables": stageVariables or {},
        "body": body,
        "isBase64Encoded": isBase64Encoded,
    }
    return res


class CognitoIdentity:
    cognito_identity_id: str | None
    cognito_identity_pool_id: str | None


class AwsLambdaContextClientContext:
    """AwsLambdaContextClientContext to use for typing or tests.

    This is not the true object used by AWS to invoke lambda handlers. This is
    here for typing, reference and testing reasons.
    """

    installation_id: str
    app_title: str
    app_version_name: str
    app_version_code: str
    app_package_name: str
    custom: dict
    env: dict


class LambdaContext:
    """LambdaContext to use for typing or tests.

    This is not the true object used by AWS to invoke lambda handlers. This is
    here for typing, reference and testing reasons.
    """

    get_remaining_time_in_millis: Callable[[], int]
    function_name: str
    function_version: str
    invoked_function_arn: str
    memory_limit_in_mb: float
    aws_request_id: str
    log_group_name: str
    log_stream_name: str
    identity: CognitoIdentity
    client_context: AwsLambdaContextClientContext | None


class ApiGatewayLambdaResponse(TypedDict, total=False):
    statusCode: HTTPStatus
    headers: dict[str, str]
    isBase64Encoded: bool
    multiValueHeaders: dict[str, list[str]]
    body: str
