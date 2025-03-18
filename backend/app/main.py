from fastapi import FastAPI
from app.views import hello

app = FastAPI()

app.include_router(hello.router)