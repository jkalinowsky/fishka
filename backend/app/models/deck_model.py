from app.database import database
from sqlalchemy import Column, Integer, String, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship

class Deck(database.Base):
    __tablename__ = 'deck'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    folder_id = Column(Integer, ForeignKey('folders.id'), nullable=False)
    folder = relationship("Folder", back_populates="decks")

    flashcards = relationship("Flashcard", back_populates="deck", cascade="all, delete-orphan")
