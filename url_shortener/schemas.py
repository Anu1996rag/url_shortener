from pydantic import BaseModel
from pydantic import EmailStr


class URLBase(BaseModel):
    target_url: EmailStr


class ResponseModel(URLBase):
    is_active: bool
    url: EmailStr

    class Config:
        orm_mode = True
