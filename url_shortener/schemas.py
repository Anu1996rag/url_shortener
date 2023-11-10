from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str


class ResponseModel(URLBase):
    is_active: bool
    url: str

    class Config:
        orm_mode = True
