from typing import Any

from app.models import Deck, Flashcard
from sqlalchemy.orm import Session, joinedload
from app.schemas.deck_pydantic import DeckSchema, FlashcardSchema

def create_deck_service(data, db: Session):
    try:
        deck = Deck(
            name=data["name"],
            folder_id=data["folder_id"],
        )

        for f in data['flashcards']:
            flashcard = Flashcard(
                question=f['question'],
                answer=f['answer'],
                deck=deck,
            )
            deck.flashcards.append(flashcard)

        db.add(deck)
        db.commit()
        db.refresh(deck)

        return True, None
    except Exception as e:
        db.rollback()
        return False, str(e)

def find_decks_by_name(name: str, db: Session) -> list:
    return db.query(Deck).filter(Deck.name.ilike(f"%{name}%")).all()

def find_deck_by_id(id: int, db: Session) -> Any | None:
    deck = db.query(Deck).options(joinedload(Deck.flashcards)).filter(Deck.id == id).first()

    if not deck:
        return None

    deck_schema = DeckSchema.from_orm(deck)

    return deck_schema.dict()

def remove_deck_by_id(id: int, db: Session):
    try:
        deck = db.query(Deck).filter(Deck.id == id).first()
        db.delete(deck)
        db.commit()
        return True, None
    except Exception as e:
        db.rollback()
        return False, str(e)