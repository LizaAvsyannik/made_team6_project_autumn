from typing import Union, List

from pydantic import BaseModel


class AuthorSchema(BaseModel):
    id: str
    name: str
    bio: Union[str, None] = None
    email: Union[str, None] = None

    class Config:
        orm_mode = True


class AuthorPatchSchema(BaseModel):
    name: Union[str, None] = None
    bio: Union[str, None] = None
    email: Union[str, None] = None


class AuthorSListSchema(BaseModel):
    articles: Union[List[AuthorSchema], None] = None
