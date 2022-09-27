from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from application.initializer import get_db_and_base
# from backend.application.initializer import (db_instance, logger_instance)

db = get_db_and_base()
router = APIRouter(prefix='/article')
# logger = logger_instance.get_logger(__name__)


@router.get('/')
async def get_article_info():
    #logger.info('Health Check')
    #await _db.insert_single_db_record({"Status": "OK"})
    return JSONResponse(content='OK', status_code=200)
