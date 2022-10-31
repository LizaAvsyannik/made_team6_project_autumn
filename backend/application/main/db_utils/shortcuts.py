import json

from sqlalchemy.exc import IntegrityError
from tqdm import tqdm

from application.initializer import get_db_and_base
from application.main.db_utils.json_reader import value_or_None, \
    publications_reader
from application.main.models.models import (
    Article,
    Author,
    AuthorInArticle,
    FieldOfScience,
    FosInArticle,
    Keyword,
    KeywordInArticle,
)


def try_eval(obj):
    try:
        return eval(obj)
    except:
        return obj


def add_article(session, entry):
    article = Article(
        id=entry["_id"],
        title=value_or_None(entry, "title"),
        abstract=value_or_None(entry, "abstract"),
        year=value_or_None(entry, "year"),
        url=value_or_None(entry, "url"),
        n_citation=value_or_None(entry, "n_citation"),
        page_start=value_or_None(entry, "page_start"),
        page_end=value_or_None(entry, "page_end"),
        topic=value_or_None(entry, "topic"),
    )
    try:
        session.add(article)
        session.commit()
    except IntegrityError:
        session.rollback()


def add_authors(session, entry):
    article_id = entry["_id"]
    authors = try_eval(value_or_None(entry, "authors"))
    if authors is None:
        return
    for author_entry in authors:
        author_id = value_or_None(author_entry, "_id")
        if author_id is None:
            return

        author = Author(
            id=author_entry["_id"],
            name=value_or_None(author_entry, "name"),
            bio=value_or_None(author_entry, "bio"),
            email=value_or_None(author_entry, "email"),
        )
        try:
            if session.query(Author).get(author_id) is None:
                session.add(author)
            session.add(AuthorInArticle(author_id=author_id, article_id=article_id))
            session.commit()
        except IntegrityError as ex:
            session.rollback()


def add_keywords(session, entry):
    article_id = entry["_id"]
    keywords = try_eval(value_or_None(entry, "keywords"))
    if isinstance(keywords, str):
        keywords = eval(keywords)
    if keywords is None:
        return
    for kw in list(map(str.lower, keywords)):
        try:
            if session.query(Keyword).filter_by(name=kw).first() is None:
                keyword = Keyword(name=kw)
                session.add(keyword)
                session.commit()
            keyword = session.query(Keyword).filter_by(name=kw)[0]
            session.add(
                KeywordInArticle(keyword_id=keyword.keyword_id, article_id=article_id)
            )
            session.commit()
        except IntegrityError as ex:
            session.rollback()


def add_fos(session, entry):
    article_id = entry["_id"]
    foss = try_eval(value_or_None(entry, "fos"))
    if foss is None:
        return
    for fos in list(map(str.lower, foss)):
        try:
            if session.query(FieldOfScience).filter_by(name=fos).first() is None:
                fieldofscience = FieldOfScience(name=fos)
                session.add(fieldofscience)
                session.commit()
            fieldofscience = session.query(FieldOfScience).filter_by(name=fos)[0]
            session.add(
                FosInArticle(fos_id=fieldofscience.fos_id, article_id=article_id)
            )
            session.commit()
        except IntegrityError as ex:
            session.rollback()


def fill_db(filename: str, use_generator, limit=100000):
    session = next(get_db_and_base())
    if use_generator:
        publications = publications_reader(filename, limit=limit)
    else:
        with open(filename) as file:
            publications = json.load(file)[:limit]
    for entry in tqdm(publications):
        add_article(session, entry)
        add_authors(session, entry)
        add_keywords(session, entry)
        add_fos(session, entry)
