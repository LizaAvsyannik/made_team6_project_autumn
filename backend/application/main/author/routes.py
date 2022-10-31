from typing import Union

from fastapi import Path, Depends, Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates

from application.initializer import db
from application.main.auth.jwt import get_current_user
from application.main.models.models import Author, User
from application.main.utils import (
    db_get_one_or_none,
    raise_error,
    db_get_all,
    db_delete_item,
)
from .schemas import AuthorSchema, AuthorPatchSchema
from .utils import db_create_author, db_update_author

templates = Jinja2Templates(directory="application/templates")

router = APIRouter(prefix="/author")


# logger = logger_instance.get_logger(__name__)


@router.get("/")
async def get_author_list(request: Request, page: Union[int, None] = 1):
    authors = db_get_all(db, Author)
    output_list = []
    start_index = (page - 1) * 10
    end_index = min(len(authors), start_index + 10)
    for index in range(start_index, end_index):
        output_list.append(authors[index])
    max_page = len(authors) // 10 + 1
    page_list = [i for i in range(max(1, page - 2), min(max_page + 1, page + 2))]
    return templates.TemplateResponse(
        "authors.html", {"request": request, "authors": output_list, "pages": page_list,
                         "cur_page": page}
    )


@router.get("/{author_id}", response_model=AuthorSchema)
async def get_author_info(
        request: Request,
        author_id: str = Path(title="The ID of the author to get")
):
    item = db_get_one_or_none(db, Author, "id", author_id)
    if item is None:
        raise_error(404, f"Author with id={author_id} not found")
    return templates.TemplateResponse(
        "author.html", {"request": request, "author": item}
    )


@router.post("/", response_model=AuthorSchema)
async def create_new_author(
        item: AuthorSchema, current_user: User = Depends(get_current_user)
):
    if db_get_one_or_none(db, Author, "id", item.id) is not None:
        raise_error(400, f"Author with id={item.id} already exists")
    return db_create_author(db, item)


@router.patch("/{author_id}", response_model=AuthorSchema)
async def modify_author(
        upd_item: AuthorPatchSchema,
        author_id: str = Path(title="The ID of the author to patch"),
        current_user: User = Depends(get_current_user),
):
    item = db_get_one_or_none(db, Author, "id", author_id)
    if item is None:
        raise_error(404, f"Author with id={author_id} not found")
    item = db_update_author(db, item, upd_item.dict(exclude_unset=True))
    return item


@router.delete("/{author_id}", response_model=AuthorSchema)
async def delete_author(
        author_id: str = Path(title="The ID of the author to delete"),
        current_user: User = Depends(get_current_user),
):
    item = db_get_one_or_none(db, Author, "id", author_id)
    if item is None:
        raise_error(404, f"Author with id={author_id} not found")
    item = db_delete_item(db, item)
    return item
