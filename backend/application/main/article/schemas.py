from typing import Union, List

from pydantic import BaseModel


class ArticleSchema(BaseModel):
    id: str
    title: Union[str, None] = None
    venue_id: str
    year: Union[int, None] = None
    n_citation: Union[int, None] = None
    abstract: Union[str, None] = None
    url: Union[str, None] = None
    publisher_id: str
    page_start: Union[str, None] = None
    page_end: Union[str, None] = None

    class Config:
        orm_mode = True


class ArticlePatchSchema(BaseModel):
    title: Union[str, None] = None
    venue_id: Union[str, None] = None
    year: Union[int, None] = None
    n_citation: Union[int, None] = None
    abstract: Union[str, None] = None
    url: Union[str, None] = None
    publisher_id: Union[str, None] = None
    page_start: Union[str, None] = None
    page_end: Union[str, None] = None


class ArticleListSchema(BaseModel):
    articles: Union[List[ArticleSchema], None] = None
