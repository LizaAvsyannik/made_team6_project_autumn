from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from .schemas import AuthorSchema, AuthorSListSchema
from typing import Union
from fastapi import Path
# from backend.application.initializer import (db_instance, logger_instance)

# _db = db_instance
router = APIRouter(prefix='/author')
# logger = logger_instance.get_logger(__name__)


@router.get('/')
async def get_author_list(page: Union[int, None] = 0):
    output_list = []
    start_index = page * 10
    end_index = min(100, start_index + 10)
    for index in range(start_index, end_index):
        output_list.append(AuthorSchema(id=index, name=f'AuthorName_{index}'))
    return AuthorSListSchema(articles=output_list)


@router.get('/{author_id}', response_model=AuthorSchema)
async def get_author_info(article_id: int = Path(title="The ID of the author to get", ge=0)):
    return AuthorSchema(id=article_id, name=f"Name_{article_id}")


@router.post('/', response_model=AuthorSchema)
async def create_new_author(item: AuthorSchema):
    import random
    item.name = f"Name_{random.randint(0, 1000)}"
    return item


@router.patch('/{author_id}', response_model=AuthorSchema)
async def modify_author(author_id: int = Path(title="The ID of the author to patch", ge=0)):
    return AuthorSchema(id=author_id, name=f"Patched_Name_{author_id}")


@router.delete('/{author_id}')
async def delete_author(author_id: int = Path(title="The ID of the author to delete", ge=0)):
    return JSONResponse(content="OK", status_code=200)
