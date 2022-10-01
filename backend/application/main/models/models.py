from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from application.initializer import get_db_and_base, Base

db = get_db_and_base()


class Venue(Base):
    __tablename__ = "venue"

    venue_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)


class Publisher(Base):
    __tablename__ = "publisher"

    publisher_id = Column(String, primary_key=True, index=True)
    issn = Column(String, nullable=True)
    isbn = Column(String, nullable=True)
    doi = Column(String, nullable=True)
    language = Column(String, nullable=True)
    volume = Column(String, nullable=True)


class AuthorInArticle(Base):
    __tablename__ = "author_in_article"
    author_id = Column(String, ForeignKey('author.id'), primary_key=True)
    article_id = Column(String, ForeignKey('article.id'), primary_key=True)


# publications_authors = Table(
#     "author_in_article",
#     Base.metadata,
#     Column("article", ForeignKey("article.article_id"), primary_key=True),
#     Column("author", ForeignKey("author.id"), primary_key=True),
# )


class Article(Base):
    __tablename__ = "article"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    venue_id = Column(String, ForeignKey(Venue.venue_id))
    n_citation = Column(Integer, default=0)
    abstract = Column(String, nullable=True)
    url = Column(String, nullable=True)
    publisher_id = Column(String, ForeignKey(Publisher.publisher_id))
    page_start = Column(String, nullable=True)
    page_end = Column(String, nullable=True)

    authors = relationship(
        "Author", secondary=AuthorInArticle.__table__, back_populates='articles'
    )


class Author(Base):
    __tablename__ = "author"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    email = Column(String, nullable=True)

    articles = relationship(
        "Article", secondary=AuthorInArticle.__table__, back_populates='authors'
    )

#
#
# class ArticleReference(Base):
#     __tablename__ = "article_reference"
#
#     article_id = Column(Integer, ForeignKey(Article.article_id), primary_key=True)
#     ref_id = Column(Integer, ForeignKey(Article.article_id), nullable=True)

#
# class Keyword(Base):
#     __tablename__ = "keyword"
#
#     keyword_id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False, unique=True)
#
#
# class FieldOfScience(Base):
#     __tablename__ = "field_of_study"
#
#     fos_id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False, unique=True)
#
#
# class KeywordInArticle(Base):
#     __tablename__ = "keyword_in_article"
#
#     keyword_id = Column(Integer, ForeignKey(Keyword.keyword_id), primary_key=True)
#     article_id = Column(Integer, ForeignKey(Article.article_id), primary_key=True)
#
#
# class FosInArticle(Base):
#     __tablename__ = "fos_in_article"
#
#     fos_id = Column(Integer, ForeignKey(FieldOfScience.fos_id), primary_key=True)
#     article_id = Column(Integer, ForeignKey(Article.article_id), primary_key=True)
#
#
# class Organisation(Base):
#     __tablename__ = "organisation"
#
#     organisation_id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False, unique=True)

#
