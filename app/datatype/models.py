import uuid
from sqlalchemy import Column, String, Integer, DateTime
from app.initializer.db import DeclBase
import datetime

# class User(DeclBase):
#     __tablename__ = "users"
#     id = Column(String(20), primary_key=True, default=lambda: str(uuid.uuid4())[:20], comment="用户 ID")
#     username = Column(String(16), unique=True, nullable=False, comment="用户名")
#     password = Column(String(128), nullable=False, comment="密码")


class User(DeclBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    username = Column(String(16), unique=True, nullable=False, comment="用户名")
    password = Column(String(128), nullable=False, comment="密码")
    nickname = Column(String(32), default="", comment="昵称")
    email = Column(String(64), default="", comment="邮箱")
    userPic = Column(String(256), default="", comment="头像地址")
    createTime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    updateTime = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment="更新时间")