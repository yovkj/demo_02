from app.datatype.models import User
from app.initializer.db import get_db_session
from sqlalchemy.exc import NoResultFound
import hashlib
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.initializer.conf import g  # 确保配置正确引入

from fastapi import HTTPException

# 从配置获取，此处示例值，实际需配置
SECRET_KEY = "your-secret-key-123456"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_user(username: str, password: str):
    with next(get_db_session()) as session:
        try:
            user = session.query(User).filter(User.username == username).one()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            return hashed_password == user.password
        except NoResultFound:
            return False


# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, g.SECRET_KEY, algorithms=[g.ALGORITHM])
#         return payload.get("sub")
#     except JWTError:
#         raise HTTPException(status_code=401, detail="无效的令牌")


def verify_token(token: str):
    try:
        payload = jwt.decode(token, g.SECRET_KEY, algorithms=[g.ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="无效的令牌")