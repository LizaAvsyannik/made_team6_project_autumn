from typing import Union, List
from application.main.author.schemas import AuthorSchema
from pydantic import BaseModel


class VenueSchema(BaseModel):
    venue_id: str
    name: Union[str, None]


class PublisherSchema(BaseModel):
    publisher_id: str
    issn: Union[str, None]
    isbn: Union[str, None]
    doi: Union[str, None]
    language: Union[str, None]
    volume: Union[str, None]


class ArticleSchema(BaseModel):
    id: str
    title: Union[str, None] = None
    venue: Union[VenueSchema, None] = None
    year: Union[int, None] = None
    n_citation: Union[int, None] = None
    abstract: Union[str, None] = None
    url: Union[str, None] = None
    publisher: Union[PublisherSchema, None] = None
    page_start: Union[str, None] = None
    page_end: Union[str, None] = None

    authors: List[AuthorSchema] = None
    fos: Union[List[str], None] = None
    keywords: Union[List[str], None] = None

    class Config:
        orm_mode = True


class ParsedFOSAndKeywordSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ArticleOutSchema(BaseModel):
    id: str
    title: Union[str, None] = None
    venue: Union[VenueSchema, None] = None
    year: Union[int, None] = None
    n_citation: Union[int, None] = None
    abstract: Union[str, None] = None
    url: Union[str, None] = None
    publisher: Union[PublisherSchema, None] = None
    page_start: Union[str, None] = None
    page_end: Union[str, None] = None

    authors: List[AuthorSchema] = None
    fos: Union[List[ParsedFOSAndKeywordSchema], None] = None
    keywords: Union[List[ParsedFOSAndKeywordSchema], None] = None

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
