from fastapi import APIRouter, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="")
templates = Jinja2Templates(directory="application/templates")


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
