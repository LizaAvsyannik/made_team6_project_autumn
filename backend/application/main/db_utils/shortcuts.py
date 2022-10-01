from sqlalchemy import MetaData

from application.initializer import engine
from sqlalchemy.exc import IntegrityError
from tqdm import tqdm

from application.main.db_utils.json_reader import value_or_None, publications_reader
from application.main.models.models import *


def drop_all_tables():
    metadata_obj = MetaData(bind=engine)
    metadata_obj.drop_all(
        tables=[
            Author.__table__,
            AuthorInArticle.__table__,
            Article.__table__,
            Venue.__table__,
            Publisher.__table__,
        ]
    )


def fill_db(filename: str, limit=10000):
    session = next(get_db_and_base())
    reader = publications_reader(filename, limit=limit)
    for entry in tqdm(reader):

        # add article
        article = Article(
            id=entry["_id"],
            title=value_or_None(entry, "title"),
            abstract=value_or_None(entry, "abstract"),
            year=value_or_None(entry, "year"),
            url=value_or_None(entry, "url"),
            n_citation=value_or_None(entry, "n_citation"),
            page_start=value_or_None(entry, "page_start"),
            page_end=value_or_None(entry, "page_end"),
        )
        session.add(article)
        session.commit()

        # add authors
        authors_dict = value_or_None(entry, "authors")

        if not authors_dict is None:
            authors = []
            for author_entry in authors_dict:
                try:
                    # Some authors don't have id
                    author_id = value_or_None(author_entry, "_id")
                    if author_id is None:
                        continue
                    author = Author(
                        id=author_entry["_id"],
                        name=value_or_None(author_entry, "name"),
                        bio=value_or_None(author_entry, "bio"),
                        email=value_or_None(author_entry, "email"),
                    )
                    if session.query(Author).get(author_id) is None:
                        authors.append(author)
                    else:
                        session.add(AuthorInArticle(author_id=author_id, article_id=article.id))
                        session.flush()
                except Exception as ex:
                    print(ex)
                    session.rollback()
                    continue
            try:
                art_to_extend = session.query(Article).get(article.id)
                art_to_extend.authors.extend(authors)
                session.flush()
            except Exception as ex:
                print(ex)
                session.rollback()
                continue
