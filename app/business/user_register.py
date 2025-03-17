from app.datatype.models import User
from app.initializer.db import get_db_session
from sqlalchemy.exc import IntegrityError
import hashlib

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str):
    # 使用 with 语句来管理会话
    with next(get_db_session()) as session:
        try:
            hashed_password = hash_password(password)
            new_user = User(username=username, password=hashed_password)
            session.add(new_user)
            session.commit()
            return True
        except IntegrityError:
            session.rollback()
            return False