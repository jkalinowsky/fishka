from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.database import get_db
from app.services.temp_user_service import create_session, check_access

router = APIRouter()

@router.post("/create-session")
async def create_temp_session(request: Request, db: Session = Depends(get_db)):
    data = await request.json()

    if not data or 'password' not in data:
        raise HTTPException(status_code=400, detail="Missing password")

    session_id, message = create_session(db, data['password'])
    if not session_id:
        raise HTTPException(status_code=401, detail=message)

    return JSONResponse({"session_id": session_id, "message": message})

@router.post("/check-access")
async def check_folder_access(request: Request, db: Session = Depends(get_db)):
    data = await request.json()

    if not data or 'session_id' not in data or 'folder_id' not in data:
        raise HTTPException(status_code=400, detail="Missing session or folder")

    has_access, message = check_access(db, data['session_id'], data['folder_id'])
    if not has_access:
        raise HTTPException(status_code=403, detail=message)

    return JSONResponse({"access": has_access, "message": message })