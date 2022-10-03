from fastapi import HTTPException
from sqlalchemy.orm import Session


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
