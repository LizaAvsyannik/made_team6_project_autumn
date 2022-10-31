from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from application.initializer import Base
from application.main.user import hashing


class Venue(Base):
    __tablename__ = "venue"

    venue_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)

    articles = relationship(
        "Article",
        back_populates="venue"
    )


class AuthorInArticle(Base):
    __tablename__ = "author_in_article"
    author_id = Column(String, ForeignKey("author.id"), primary_key=True)
    article_id = Column(String, ForeignKey("article.id"), primary_key=True)


class Author(Base):
    __tablename__ = "author"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    email = Column(String, nullable=True)

    articles = relationship(
        "Article",
        secondary=AuthorInArticle.__table__,
        back_populates="authors"
    )

    def __repr__(self):
        return f'{self.id} {self.name}'


class ArticleReference(Base):
    __tablename__ = "article_reference"

    article_id = Column(String, ForeignKey("article.id"), primary_key=True)
    ref_id = Column(String, ForeignKey("article.id"), nullable=True)


class KeywordInArticle(Base):
    __tablename__ = "keyword_in_article"

    keyword_id = Column(
        Integer,
        ForeignKey("keyword.keyword_id"),
        primary_key=True
    )
    article_id = Column(String, ForeignKey("article.id"), primary_key=True)


class FosInArticle(Base):
    __tablename__ = "fos_in_article"
    fos_id = Column(
        Integer,
        ForeignKey("field_of_study.fos_id"),
        primary_key=True
    )
    article_id = Column(String, ForeignKey("article.id"), primary_key=True)


class Keyword(Base):
    __tablename__ = "keyword"

    keyword_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True, index=True)
    articles = relationship(
        "Article",
        secondary=KeywordInArticle.__table__,
        back_populates="keywords"
    )

    def __repr__(self):
        return f'{self.keyword_id} {self.name}'


class FieldOfScience(Base):
    __tablename__ = "field_of_study"
    fos_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True, index=True)
    articles = relationship(
        "Article",
        secondary=FosInArticle.__table__,
        back_populates="fos"
    )

    def __repr__(self):
        return f'{self.fos_id} {self.name}'


# class Organisation(Base):
#     __tablename__ = "organisation"
#
#     organisation_id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False, unique=True)


class Article(Base):
    __tablename__ = "article"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    venue_id = Column(String, ForeignKey(Venue.venue_id), nullable=True)
    n_citation = Column(Integer, default=0)
    abstract = Column(String, nullable=True)
    url = Column(String, nullable=True)

    page_start = Column(String, nullable=True)
    page_end = Column(String, nullable=True)
    topic = Column(String, nullable=True)

    authors = relationship(
        "Author",
        secondary=AuthorInArticle.__table__,
        back_populates="articles"
    )
    fos = relationship(
        "FieldOfScience",
        secondary=FosInArticle.__table__,
        back_populates="articles"
    )
    keywords = relationship(
        "Keyword",
        secondary=KeywordInArticle.__table__,
        back_populates="articles"
    )
    venue = relationship(
        "Venue",
        back_populates="articles"
    )

    def __repr__(self):
        return f'{self.id} {self.title} \n {str(self.authors) } \n {str(self.keywords) } \n {str(self.fos)}'


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))

    def __init__(self, name, email, password, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = hashing.get_password_hash(password)

    def check_password(self, password):
        return hashing.verify_password(self.password, password)
