from application.initializer import get_db_and_base
from application.main.config import Config
from application.main.db_utils.shortcuts import fill_db
from application.main.models.models import Article
import logging

session = next(get_db_and_base())

logger = logging.getLogger()
logger.info("This is test")

if session.query(Article).first() is None:
    session.close()
    print("Creating database...")
    fill_db(Config.DB_SOURCE_FILE, use_generator=False, limit=10_000)
else:
    print("Database already exists")
    session.close()
