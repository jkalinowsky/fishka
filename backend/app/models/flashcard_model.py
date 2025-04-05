from app.database import database
from sqlalchemy import Column, Integer, String, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship

class Flashcard(database.Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True, nullable=False)

    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)

    deck_id = Column(Integer, ForeignKey("deck.id", ondelete="CASCADE"), nullable=False)

    deck = relationship("Deck", back_populates="flashcards")