from functools import reduce
from typing import Union

from fastapi import Path, Depends, Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates

from application.initializer import db
from application.main.auth.jwt import get_current_user
from application.main.models.models import Article, User
from application.main.utils import (
    db_get_one_or_none,
    raise_error,
    db_delete_item,
    db_get_all,
    db_get_article_by_filters
)
from .schemas import (
    ArticleSchema,
    ArticleListSchema,
    ArticlePatchSchema,
    ArticleOutSchema,
)
from .utils import db_create_article, db_update_article

templates = Jinja2Templates(directory="application/templates")

router = APIRouter(prefix="/article")


@router.get("/", response_model=ArticleListSchema)
async def get_article_list(
        request: Request,
        page: Union[int, None] = 1,
        year: Union[int, None] = None,
        venue: Union[str, None] = None,
        author: Union[str, None] = None,
        topic: Union[str, None] = None
):
    cond = reduce(lambda x, y: x and y, [item is None for item in [year, venue, author, topic]])
    if cond:
        articles = db_get_all(db, Article)
    else:
        articles = db_get_article_by_filters(
            db,
            year,
            venue,
            author,
            topic
            )
    output_list = []
    start_index = (page - 1) * 10
    end_index = min(len(articles), start_index + 10)
    for index in range(start_index, end_index):
        output_list.append(articles[index])
    max_page = len(articles) // 10 + 1
    page_list = [i for i in range(max(1, page - 2), min(max_page + 1, page + 2))]
    return templates.TemplateResponse(
        "articles.html", {"request": request, "articles": output_list, "pages": page_list,
                          "cur_page": page}
    )


@router.get("/{article_id}", response_model=ArticleOutSchema)
async def get_article_info(
        request: Request,
        article_id: str = Path(title="The ID of the article to get"),
):
    item = db_get_one_or_none(db, Article, "id", article_id)
    if item is None:
        raise_error(404, f"Article with id={article_id} not found")
    return templates.TemplateResponse(
        "article.html", {"request": request, "article": item}
    )


@router.post("/", response_model=ArticleOutSchema)
async def create_new_article(item: ArticleSchema):
    if db_get_one_or_none(db, Article, "id", item.id) is not None:
        raise_error(400, f"Author with id={item.id} already exists")
    return db_create_article(db, item)


@router.patch("/{article_id}", response_model=ArticleOutSchema)
async def modify_article(
        upd_item: ArticlePatchSchema,
        article_id: str = Path(title="The ID of the article to patch"),
        current_user: User = Depends(get_current_user),
):
    item = db_get_one_or_none(db, Article, "id", article_id)
    if item is None:
        raise_error(404, f"Article with id={article_id} not found")
    item = db_update_article(db, item, upd_item.dict(exclude_unset=True))
    return item


@router.delete("/{article_id}", response_model=ArticleOutSchema)
async def delete_article(
        article_id: str = Path(title="The ID of the article to delete"),
        current_user: User = Depends(get_current_user),
):
    item = db_get_one_or_none(db, Article, "id", article_id)
    if item is None:
        raise_error(404, f"Article with id={article_id} not found")
    item = db_delete_item(db, item)
    return item
