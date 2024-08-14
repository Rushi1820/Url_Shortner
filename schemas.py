from pydantic import BaseModel


class URLBase(BaseModel):
    original_url: str

class URLCreate(URLBase):
    pass

class URLResponse(BaseModel):
    original_url: str
    short_code: str

    class Config:
        orm_mode = True


