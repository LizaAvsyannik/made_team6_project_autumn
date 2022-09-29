from typing import Union, List

from pydantic import BaseModel


class AuthorSchema(BaseModel):
    id: int
    name: str


class AuthorSListSchema(BaseModel):
    articles: Union[List[AuthorSchema], None] = None
