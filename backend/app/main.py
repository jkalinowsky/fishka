from fastapi import FastAPI
from app.views import deck_views
from app.database import create_tables

app = FastAPI()

create_tables()

app.include_router(deck_views.router)