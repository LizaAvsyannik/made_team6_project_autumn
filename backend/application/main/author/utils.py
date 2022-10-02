from sqlalchemy.orm import Session
from application.main.models.models import Author
from .schemas import AuthorSchema, AuthorPatchSchema


def db_create_author(db: Session, author: AuthorSchema):
    item = Author(
        id=author.id,
        name=author.name,
        bio=author.bio,
        email=author.email
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def db_update_author(db: Session, item: Author, new_data: dict):
    if 'email' in new_data:
        item.email = new_data['email']
    if 'bio' in new_data:
        item.bio = new_data['bio']
    if 'name' in new_data:
        item.name = new_data['name']
    db.commit()
    db.refresh(item)
    return item


def db_delete_author(db: Session, item: Author):
    db.delete(item)
    db.commit()
    return item

