from pydantic import BaseModel
from typing import List

class FlashcardSchema(BaseModel):
    id: int
    question: str
    answer: str

    class Config:
        from_attributes = True

class DeckSchema(BaseModel):
    id: int
    name: str
    flashcards: List[FlashcardSchema]

    class Config:
        from_attributes = True