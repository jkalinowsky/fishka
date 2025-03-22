from fastapi import APIRouter, Request, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.services.folder_service import create_folder_service, find_folder_by_name
from app.database import get_db

router = APIRouter()

# not secured, right now for testing
@router.post("/create-folder")
async def create_folder(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    if not data or not 'name' in data or not 'password' in data:
        raise HTTPException(status_code=400, detail="Invalid data format.")
    success, message = create_folder_service(data, db)

    if not success:
        raise HTTPException(status_code=404, detail=message)
    return JSONResponse(content={"Message": "Ok"}, status_code=201)

@router.get("/folder/find")
async def find_folder(name: str, db: Session = Depends(get_db)):
    folders = find_folder_by_name(name, db)

    if not folders:
        raise HTTPException(status_code=404, detail="Folder not found.")
    return JSONResponse(content={
        "folders": [{"name": folder.name, "id": folder.id} for folder in folders]
    })

