from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from application.main.config import Config


class IncludeAPIRouter(object):
    def __new__(cls):
        from application.main.article.routes import router as article_router
        from application.main.author.routes import router as author_router
        from application.main.auth.routes import router as auth_router
        from application.main.user.routes import router as user_router
        from application.main.index.routes import router as index_router
        from fastapi.routing import APIRouter

        router = APIRouter()
        router.include_router(article_router, tags=["article"])
        router.include_router(author_router, tags=["author"])
        router.include_router(auth_router, tags=["auth"])
        router.include_router(user_router, tags=["user"])
        router.include_router(index_router, tags=["index"])
        return router


engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db_and_base():
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db = next(get_db_and_base())
