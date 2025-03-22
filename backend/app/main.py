from fastapi import FastAPI
from app.views import deck_views, temp_users_views, folder_views
from app.database import create_tables

app = FastAPI()

create_tables()

app.include_router(deck_views.router)
app.include_router(temp_users_views.router)
app.include_router(folder_views.router)