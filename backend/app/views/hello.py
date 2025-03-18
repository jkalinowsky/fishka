from fastapi import APIRouter
from app.services.hello_service import get_hello

router = APIRouter()

@router.get("/hello-world")
def hello_world():
    return {"message": get_hello()}