from app.models import Deck, Flashcard, Folder, TempUserSession
from sqlalchemy.orm import Session, joinedload
from uuid import uuid4
from datetime import datetime, timedelta
from app.core.utils import verify_password

def create_session(db: Session, password: str, duration_minutes: int = 60):
    try:
        folders = db.query(Folder).all()

        for folder in folders:
            if verify_password(password, folder.hashed_password):
                session_id = str(uuid4())
                expires_at = datetime.utcnow() + timedelta(minutes=duration_minutes)
                temp_user = TempUserSession(
                    session_id=session_id,
                    access_id=folder.access_id,
                    expires_at=expires_at,
                )
                db.add(temp_user)
                db.commit()
                return session_id, "Temporary user session created."
        return None, "Invalid password."
    except Exception as e:
        db.rollback()
        return None, str(e)


def check_access(db: Session, session_id: str, folder_id: int):
    try:
        temp_session = db.query(TempUserSession).filter_by(session_id=session_id).first()

        if temp_session is None or temp_session.expires_at < datetime.utcnow():
            return False, 'Session expired.'

        folder = db.query(Folder).filter_by(id=folder_id).first()
        if folder is None:
            return False, 'No access for this session.'

        if temp_session.access_id == folder.access_id:
            return True, 'Access granted.'
        return False, 'Access denied.'
    except Exception as e:
        db.rollback()
        return None, str(e)