from sqlalchemy.orm import Session
from application.main.models.models import Article, Venue, Publisher, Author, Keyword, FieldOfScience
from .schemas import ArticleSchema
from application.main.utils import db_get_one_or_none, raise_error


def db_create_article(db: Session, article: ArticleSchema):
    venue = article.venue
    publisher = article.publisher
    venue_old = db_get_one_or_none(db, Venue, 'venue_id', venue.venue_id)
    if venue_old is None and venue is not None:
        venue_old = Venue(
            venue_id=venue.venue_id,
            name=venue.name
        )
        db.add(venue_old)
    publisher_old = db_get_one_or_none(db, Publisher, 'publisher_id', publisher.publisher_id)
    if publisher_old is None and publisher is not None:
        publisher_old = Publisher(
            publisher_id=publisher.publisher_id,
            issn=publisher.issn,
            isbn=publisher.isbn,
            doi=publisher.doi,
            language=publisher.language,
            volume=publisher.volume
        )
        db.add(publisher_old)
    item = Article(
        id=article.id,
        title=article.title,
        venue_id=venue_old.venue_id,
        year=article.year,
        n_citation=article.n_citation,
        abstract=article.abstract,
        url=article.url,
        publisher_id=publisher_old.publisher_id,
        page_start=article.page_start,
        page_end=article.page_end
    )
    for author in article.authors:
        new_author = db_get_one_or_none(db, Author, 'id', author.id)
        if new_author is None:
            new_item = Author(
                id=author.id,
                name=author.name,
                bio=author.bio,
                email=author.email
            )
            item.authors.append(new_item)
        else:
            item.authors.append(new_author)
    for keyword in article.keywords:
        old_keyword = db_get_one_or_none(db, Keyword, 'name', keyword.lower())
        if old_keyword is None:
            new_item = Keyword(name=keyword.lower())
            item.keywords.append(new_item)
        else:
            item.keywords.append(old_keyword)
    for fos in article.fos:
        old_fos = db_get_one_or_none(db, FieldOfScience, 'name', fos.lower())
        if old_fos is None:
            new_item = FieldOfScience(name=fos.lower())
            item.fos.append(new_item)
        else:
            item.fos.append(old_fos)
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
