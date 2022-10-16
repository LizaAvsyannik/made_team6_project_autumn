from fastapi.routing import APIRouter
from fastapi import Path
from typing import Union
from .utils import db_create_article, db_update_article
from .schemas import ArticleSchema, ArticleListSchema, ArticlePatchSchema, ArticleOutSchema
from application.main.models.models import Article
from application.initializer import db
from application.main.utils import db_get_one_or_none, raise_error, db_delete_item, db_get_all

router = APIRouter(prefix='/article')
# logger = logger_instance.get_logger(__name__)


@router.get('/', response_model=ArticleListSchema)
async def get_article_list(page: Union[int, None] = 0):
    articles = db_get_all(db, Article)
    output_list = []
    start_index = page * 10
    end_index = min(len(articles), start_index + 10)
    for index in range(start_index, end_index):
        output_list.append(articles[index])
    return ArticleListSchema(articles=output_list)


@router.get('/{article_id}', response_model=ArticleOutSchema)
async def get_article_info(article_id: str = Path(title="The ID of the article to get")):
    item = db_get_one_or_none(db, Article, 'id', article_id)
    if item is None:
        raise_error(404, f'Article with id={article_id} not found')
    print(item.fos[0].name)
    print(item.fos[1].name)
    return item


@router.post('/', response_model=ArticleOutSchema)
async def create_new_article(item: ArticleSchema):
    if db_get_one_or_none(db, Article, 'id', item.id) is not None:
        raise_error(400, f'Author with id={item.id} already exists')
    return db_create_article(db, item)


@router.patch('/{article_id}', response_model=ArticleOutSchema)
async def modify_article(upd_item: ArticlePatchSchema,
                         article_id: str = Path(title="The ID of the article to patch")):
    item = db_get_one_or_none(db, Article, 'id', article_id)
    if item is None:
        raise_error(404, f'Article with id={article_id} not found')
    item = db_update_article(db, item, upd_item.dict(exclude_unset=True))
    return item


@router.delete('/{article_id}', response_model=ArticleOutSchema)
async def delete_article(article_id: str = Path(title="The ID of the article to delete")):
    item = db_get_one_or_none(db, Article, 'id', article_id)
    if item is None:
        raise_error(404, f'Article with id={article_id} not found')
    item = db_delete_item(db, item)
    return item
