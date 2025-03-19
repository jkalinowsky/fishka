from app.models import Deck, Flashcard
from sqlalchemy.orm import Session

def create_deck_service(data, db: Session):
    try:
        deck = Deck(name=data["name"])

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

def find_deck_by_id(id: int, db: Session) -> Deck:
    return db.query(Deck).filter(Deck.id == id).first()

def remove_deck_by_id(id: int, db: Session):
    try:
        deck = db.query(Deck).filter(Deck.id == id).first()
        db.delete(deck)
        db.commit()
        return True, None
    except Exception as e:
        db.rollback()
        return False, str(e)