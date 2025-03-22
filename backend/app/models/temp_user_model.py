from app.database import database
from sqlalchemy import Column, Integer, String, Boolean, text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class TempUserSession(database.Base):
    __tablename__ = 'temp_users'
    id = Column(Integer, primary_key=True, nullable=False)
    session_id = Column(String, unique=True, nullable=False, index=True)
    access_id = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)