"""

"""
import sys
import os

from fastapi.responses import RedirectResponse

app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, app_dir)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.users.router import router as router_users
from app.users.router_auth import router as router_authentification
from app.pages.router import router as page_router
from app.admin_panel.router import router as admin_page_router

app = FastAPI(docs_url="/docs/api")
app.mount('/static', StaticFiles(directory='app/static'), 'static')
@app.get("/", response_class=RedirectResponse)
def home_page():
    return "/pages"


app.include_router(prefix="/api/v1", router=router_users, tags=["API v1"])
app.include_router(prefix="/api/v1", router=router_authentification, tags=["API v1", "Аутентификация"])
app.include_router(router=admin_page_router)
app.include_router(page_router)


