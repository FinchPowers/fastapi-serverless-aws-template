from typing import Annotated

import structlog
from fastapi import APIRouter, Query
from typing_extensions import TypedDict

router = APIRouter()
log = structlog.get_logger(__name__)


class Token(TypedDict):
    access_token: str
    token_type: str


@router.get("")
def get_token(
    client_id: Annotated[str, Query(description="Client ID", min_length=10, max_length=100)],
    client_secret: Annotated[
        str, Query(description="Client SECRET", min_length=10, max_length=100)
    ],
) -> Token:
    """Retrieve a JWT."""
    # only need access_token and token_type, so delete all other keys
    return {
        "access_token": "the access token",
        "token_type": "the token type",
    }
