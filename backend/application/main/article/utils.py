from sqlalchemy.orm import Session
from application.main.models.models import Article, Venue, Publisher
from .schemas import ArticleSchema
from application.main.utils import db_get_one_or_none, raise_error


def db_create_article(db: Session, article: ArticleSchema):
    id_v = article.venue_id
    id_p = article.publisher_id
    venue = db_get_one_or_none(db, Venue, 'venue_id', id_v)
    if venue is None:
        raise_error(404, f'Venue with id={id_v} not found')
    publisher = db_get_one_or_none(db, Publisher, 'publisher_id', id_p)
    if publisher is None:
        raise_error(404, f'Publisher with id={id_p} not found')
    item = Article(
        id=article.id,
        title=article.title,
        venue_id=article.venue_id,
        year=article.year,
        n_citation=article.n_citation,
        abstract=article.abstract,
        url=article.url,
        publisher_id=article.publisher_id,
        page_start=article.page_start,
        page_end=article.page_end
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def db_update_article(db: Session, item: Article, new_data: dict):
    if 'title' in new_data:
        item.title = new_data['title']
    if 'venue_id' in new_data:
        id_ = new_data['venue_id']
        venue = db_get_one_or_none(db, Venue, 'venue_id', id_)
        if venue is None:
            raise_error(404, f'Venue with id={id_} not found')
        item.venue_id = id_
    if 'year' in new_data:
        item.year = new_data['year']
    if 'n_citation' in new_data:
        item.n_citation = new_data['n_citation']
    if 'url' in new_data:
        item.url = new_data['url']
    if 'name' in new_data:
        item.name = new_data['name']
    if 'publisher_id' in new_data:
        id_ = new_data['publisher_id']
        publisher = db_get_one_or_none(db, Publisher, 'publisher_id', id_)
        if publisher is None:
            raise_error(404, f'Publisher with id={id_} not found')
        item.publisher_id = id_
    if 'page_start' in new_data:
        item.page_start = new_data['page_start']
    if 'page_end' in new_data:
        item.page_end = new_data['page_end']
    db.commit()
    db.refresh(item)
    return item
