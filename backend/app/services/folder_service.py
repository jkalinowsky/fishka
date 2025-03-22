from app.models import Folder
from app.core.utils import hash_password
from uuid import uuid4
from sqlalchemy.orm import Session

# temporary
def create_folder_service(data, db: Session):
    try:
        folder = Folder(
            name=data['name'],
            access_id=str(uuid4().hex),
            hashed_password=hash_password(data["password"]),
        )

        db.add(folder)
        db.commit()
        db.refresh(folder)

        return True, None
    except Exception as e:
        db.rollback()
        return False, str(e)

def find_folder_by_name(name: str, db: Session) -> list:
    return db.query(Folder).filter(Folder.name.ilike(f"%{name}%")).all()