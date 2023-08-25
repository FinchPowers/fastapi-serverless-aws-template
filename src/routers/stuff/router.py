from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

from src.permissions import Permissions
from src.routers.stuff.models import GetAllStuffResponse, GetSingleStuffResponse

router = APIRouter()

STUFF = ["item", "other item"]


@router.get("", response_model=GetAllStuffResponse)
def get_apis(
    permissions: Permissions,
) -> GetAllStuffResponse:
    return GetAllStuffResponse(data=dict(enumerate(STUFF)))


@router.get("", response_model=GetSingleStuffResponse)
def get_api(stuff_id: Annotated[int, Query(ge=0)]) -> GetSingleStuffResponse:
    try:
        data: str = STUFF[stuff_id]
    except IndexError:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="That index is undefined."
        ) from None
    return GetSingleStuffResponse(data=data)
