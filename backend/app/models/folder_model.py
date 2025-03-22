from app.database import database
from sqlalchemy import Column, Integer, String, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship

class Folder(database.Base):
    __tablename__ = 'folders'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    access_id = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    decks = relationship("Deck", back_populates="folder", cascade="all, delete-orphan")
