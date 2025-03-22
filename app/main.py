import sys
import os

app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, app_dir)

from fastapi import FastAPI
from app.users.router import router as router_users
from app.users.router_auth import router as router_authentification

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


app.include_router(router_users)
app.include_router(router_authentification)
