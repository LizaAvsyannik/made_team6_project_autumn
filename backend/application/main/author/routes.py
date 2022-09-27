from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

# from backend.application.initializer import (db_instance, logger_instance)

# _db = db_instance
router = APIRouter(prefix='/author')
# logger = logger_instance.get_logger(__name__)


@router.get('/')
async def get_author():
    #logger.info('Health Check')
    #await _db.insert_single_db_record({"Status": "OK"})
    return JSONResponse(content='AUTHOR', status_code=200)
