from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.initializer.conf import g

# 创建数据库引擎
engine = create_engine(g.db_url)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类
DeclBase = declarative_base()


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
