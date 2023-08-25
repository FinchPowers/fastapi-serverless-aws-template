"""Permissions module.

Technically, the authorizaation should be handled by API Gateway, so there should not be
authorization to do. That being said, the Permissions annotation should be used to
1. Make the "Authorization" protocol part of the OpenAPI specification, which in turn will make the
Authorization button appear in the UI.
2. Is the authorization scheme is a JWT, it can be used to extract the payload portion.
"""
from typing import Annotated

import structlog
from fastapi import Depends, Request, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src import runtime_info

log = structlog.get_logger(__name__)
security = Security(HTTPBearer())


def permissions(request: Request, auth: HTTPAuthorizationCredentials = security) -> dict:
    # Nothing so far. Access are manged by the authorizer
    if runtime_info.IS_RUNNING_AS_LAMBDA:
        log.debug(
            "aws permissions function invoked",
            aws_event=request.scope["aws.event"],
            aws_context=request.scope["aws.context"],
        )
    return {}


Permissions = Annotated[dict, Depends(permissions)]
