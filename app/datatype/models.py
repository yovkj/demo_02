import uuid
from sqlalchemy import Column, String
from app.initializer.db import DeclBase


class User(DeclBase):
    __tablename__ = "users"
    id = Column(String(20), primary_key=True, default=lambda: str(uuid.uuid4())[:20], comment="用户 ID")
    username = Column(String(16), unique=True, nullable=False, comment="用户名")
    password = Column(String(128), nullable=False, comment="密码")
