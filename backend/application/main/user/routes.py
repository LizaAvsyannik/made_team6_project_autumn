from fastapi import APIRouter, HTTPException, status, Depends
from application.main.models.models import User
from typing import  Union
from application.main.utils import db_get_one_or_none, db_get_all
from application.initializer import db
from application.main.user.schemas import UserSchemaInput, UserSchemaOutput, UserListSchema
from .utils import db_create_user
from application.main.auth.jwt import get_current_user


router = APIRouter(prefix='/user')


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserSchemaOutput)
async def register_user(request: UserSchemaInput):
    user = db_get_one_or_none(db, User, 'email', request.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    new_user = db_create_user(db, request)
    return new_user


@router.get('/', response_model=UserListSchema)
async def get_all_users(page: Union[int, None] = 0, current_user: User = Depends(get_current_user)):
    users = db_get_all(db, User)
    output_list = []
    start_index = page * 10
    end_index = min(len(users), start_index + 10)
    for index in range(start_index, end_index):
        output_list.append(users[index])
    return UserListSchema(users=output_list)
