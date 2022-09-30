from application.initializer import Base, engine, get_db_and_base
from application.main.models.models import *
from sqlalchemy import create_engine, insert, select, update
from sqlalchemy.orm import Session

from sqlalchemy import MetaData


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

