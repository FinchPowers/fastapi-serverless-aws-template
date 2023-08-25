from pydantic import BaseModel


class GetAllStuffResponse(BaseModel):
    data: dict[int, str]


class GetSingleStuffResponse(BaseModel):
    data: str
