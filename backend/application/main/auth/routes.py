from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

from application.initializer import db
from application.main.auth.jwt import create_access_token
from application.main.models.models import User
from application.main.user import hashing
from application.main.utils import db_get_one_or_none

router = APIRouter(prefix="/auth")
templates = Jinja2Templates(directory="templates")


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends()):
    user = db_get_one_or_none(db, User, "email", request.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password"
        )

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
