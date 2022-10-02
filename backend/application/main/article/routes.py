from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from fastapi import Path
from typing import Union
from .schemas import ArticleSchema, ArticleListSchema
# from backend.application.initializer import (db_instance, logger_instance)

router = APIRouter(prefix='/article')
# logger = logger_instance.get_logger(__name__)


@router.get('/{article_id}', response_model=ArticleSchema)
async def get_article_info(article_id: int = Path(title="The ID of the article to get", ge=0)):
    return ArticleSchema(id=article_id, name=f"Name_{article_id}")


@router.get('/', response_model=ArticleListSchema)
async def get_article_list(page: Union[int, None] = 0):
    output_list = []
    start_index = page * 10
    end_index = min(100, start_index + 10)
    for index in range(start_index, end_index):
        output_list.append(ArticleSchema(id=index, name=f'ExactName_{index}'))
    return ArticleListSchema(articles=output_list)


@router.post('/', response_model=ArticleSchema)
async def create_new_article(item: ArticleSchema):
    import random
    item.name = f"Name_{random.randint(0, 1000)}"
    return item


@router.patch('/{article_id}', response_model=ArticleSchema)
async def modify_article(article_id: int = Path(title="The ID of the article to patch", ge=0)):
    return ArticleSchema(id=article_id, name=f"Patched_Name_{article_id}")


@router.delete('/{article_id}')
async def delete_article(article_id: int = Path(title="The ID of the article to delete", ge=0)):
    return JSONResponse(content="OK", status_code=200)
