from dataclasses import dataclass


@dataclass
class Config:
    APP_NAME = 'test_application'
    APP_DESCRIPTION = 'Simple application for article savings'
    APP_VERSION = '0.1'
    #SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db_container:5432/publications_db"


app_settings = Config()
