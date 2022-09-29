from typing import Union, List

from pydantic import BaseModel


class ArticleSchema(BaseModel):
    id: int
    name: str


class ArticleListSchema(BaseModel):
    articles: Union[List[ArticleSchema], None] = None
