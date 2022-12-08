from fastapi import HTTPException


def db_get_one_or_none(db, model, field, value):
    return db.query(model).filter_by(**{field: value}).one_or_none()


def raise_error(code, message):
    raise HTTPException(status_code=code, detail=message)


def db_get_list(db, model, field, value):
    return db.query(model).filter_by(**{field: value}).all()


def db_get_all(db, model):
    return db.query(model).all()


def db_delete_item(db, item):
    db.delete(item)
    db.commit()
    return item


def db_get_article_by_filters(db, year=None, venue=None, author=None, topic=None):
    from application.main.models.models import Article, Author, Venue
    query = db.query(Article)
    if author is not None:
        query = query.join(Article.authors)
    if venue is not None:
        query = query.join(Article.venue)
    if venue is not None:
        query = query.filter(Venue.name == venue)
    if author is not None:
        query = query.filter(Author.name == author)
    if topic is not None:
        query = query.filter(Article.topic == topic)
    if year is not None:
        query = query.filter(Article.year == year)
    return query.all()
