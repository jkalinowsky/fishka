from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.services.deck_service import create_deck_service, find_decks_by_name, create_deck_service, find_deck_by_id, remove_deck_by_id
from app.database import get_db

router = APIRouter()

@router.post("/create-deck")
async def create_deck(request: Request, db: Session = Depends(get_db)):
    data = await request.json()

    if not data or 'name' not in data or 'flashcards' not in data:
        raise HTTPException(status_code=400, detail="Invalid data format")

    success, message = create_deck_service(data, db)

    if not success:
        raise HTTPException(status_code=404, detail=message)
    return JSONResponse(content={"Message": "Ok"}, status_code=201)

@router.get("/deck/find")
async def find_deck(name: str, db: Session = Depends(get_db)):
    decks = find_decks_by_name(name, db)

    if not decks:
        raise HTTPException(status_code=404, detail="No decks found.")

    return {
        "decks": [{"id": deck.id, "name": deck.name} for deck in decks]
    }, 200

@router.get("/deck")
async def get_deck(id: int, db: Session = Depends(get_db)):
    if not id:
        raise HTTPException(status_code=400, detail="No id provided.")

    deck = find_deck_by_id(id, db)

    if not deck:
        raise HTTPException(status_code=404, detail="No deck found.")

    return deck, 200

@router.post("/deck/remove")
async def remove_deck(id: int, db: Session = Depends(get_db)):
    if not id:
        raise HTTPException(status_code=400, detail="No id provided.")

    success, message = remove_deck_by_id(id, db)

    if not success:
        raise HTTPException(status_code=404, detail=message)
    return JSONResponse(content={"Message": "Ok"}, status_code=200)
