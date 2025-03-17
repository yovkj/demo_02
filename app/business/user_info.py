from app.initializer.db import get_db_session
from app.datatype.models import User
from sqlalchemy.exc import NoResultFound

def get_user_info(username: str):
    with next(get_db_session()) as session:
        try:
            user = session.query(User).filter(User.username == username).first()
            if not user:
                return None
            user_data = {
                "id": user.id,
                "username": user.username,
                "nickname": user.nickname if hasattr(user, "nickname") else "",
                "email": user.email if hasattr(user, "email") else "",
                "userPic": user.userPic if hasattr(user, "userPic") else "",
                "createTime": str(user.createTime) if hasattr(user, "createTime") else "",
                "updateTime": str(user.updateTime) if hasattr(user, "updateTime") else ""
            }
            return user_data
        except NoResultFound:
            return None