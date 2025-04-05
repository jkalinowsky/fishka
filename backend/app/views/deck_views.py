from fastapi import APIRouter, Request, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.services.deck_service import create_deck_service, find_decks_by_name, create_deck_service, find_deck_by_id, \
    remove_deck_by_id
from app.database import get_db
from app.services.temp_user_service import check_access

router = APIRouter()

async def validate_access(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    print(data)
    if not data or not 'session_id' in data or not 'folder_id' in data:
        raise HTTPException(status_code=400, detail="No session id or folder id.")

    has_access, _ = check_access(db, data['session_id'], data['folder_id'])
    print(has_access)
    if not has_access:
        raise HTTPException(status_code=403, detail="You do not have permission to perform this action.")

    return data

@router.post("/create-deck")
async def create_deck(request: Request, db: Session = Depends(get_db), data: dict = Depends(validate_access)):
    if not data or 'name' not in data or 'flashcards' not in data:
        raise HTTPException(status_code=400, detail="Invalid data format.")

    success, message = create_deck_service(data, db)

    if not success:
        raise HTTPException(status_code=404, detail=message)
    return JSONResponse(content={"Message": "Ok"}, status_code=201)

@router.get("/deck/find")
async def find_deck(request: Request, name: str, db: Session = Depends(get_db), data: dict = Depends(validate_access)):
    decks = find_decks_by_name(name, db)

    if not decks:
        raise HTTPException(status_code=404, detail="No decks found.")

    return JSONResponse(content={
        "decks": [{"id": deck.id, "name": deck.name} for deck in decks]
    })

@router.get("/deck")
async def get_deck(request: Request, id: int, db: Session = Depends(get_db), data: dict = Depends(validate_access)):
    if not id:
        raise HTTPException(status_code=400, detail="No id provided.")

    deck = find_deck_by_id(id, db)

    if not deck:
        raise HTTPException(status_code=404, detail="No deck found.")

    return JSONResponse(content=deck, status_code=200)

@router.post("/deck/remove")
async def remove_deck(request: Request, id: int, db: Session = Depends(get_db), data: dict = Depends(validate_access)):
    if not id:
        raise HTTPException(status_code=400, detail="No id provided.")

    success, message = remove_deck_by_id(id, db)

    if not success:
        raise HTTPException(status_code=404, detail=message)
    return JSONResponse(content={"Message": "Ok"}, status_code=200)
