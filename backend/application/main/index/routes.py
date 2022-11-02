from fastapi import APIRouter, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="")
templates = Jinja2Templates(directory="application/templates")


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/network")
async def network_analytics():
    import os
    root = os.path.abspath(__file__)
    splited = os.path.split(root)
    splited = os.path.split(splited[0])
    splited = os.path.split(splited[0])
    with open(os.path.join(splited[0], 'static', 'html', 'nework_graph.html')) as fh:
        data = fh.read()
    return HTMLResponse(content=data, status_code=200)


@router.get("/citation")
async def top_citation_analytics():
    import os
    root = os.path.abspath(__file__)
    splited = os.path.split(root)
    splited = os.path.split(splited[0])
    splited = os.path.split(splited[0])
    with open(os.path.join(splited[0], 'static', 'html', 'top_citation_authors.html')) as fh:
        data = fh.read()
    return HTMLResponse(content=data, status_code=200)
