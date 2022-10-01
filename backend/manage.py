from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application.initializer import IncludeAPIRouter, engine
from application.main.config import app_settings, Config
from application.main.db_utils.shortcuts import drop_all_tables, fill_db
from application.main.models.models import Base


def get_application():
    _app = FastAPI(title=app_settings.APP_NAME,
                   description=app_settings.APP_DESCRIPTION,
                   version=app_settings.APP_VERSION)
    _app.include_router(IncludeAPIRouter())
    _app.add_middleware(
        CORSMiddleware,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return _app


app = get_application()
Base.metadata.create_all(bind=engine)



@app.on_event("shutdown")
async def app_shutdown():
    # on app shutdown do something probably close some connections or trigger some event
    print("On App Shutdown i will be called.")
