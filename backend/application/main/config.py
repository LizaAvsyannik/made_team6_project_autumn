from dataclasses import dataclass


@dataclass
class Config:
    APP_NAME = 'test_application'
    APP_DESCRIPTION = 'Simple application for article savings'
    APP_VERSION = '0.1'
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


app_settings = Config()
