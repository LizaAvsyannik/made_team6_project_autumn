from sqlalchemy.orm import Session

from application.main.models.models import User
from .schemas import UserSchemaInput


def db_create_user(db: Session, user: UserSchemaInput):
    item = User(name=user.name, email=user.email, password=user.password)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
