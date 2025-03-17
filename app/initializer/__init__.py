from app.initializer.conf import g
from app.initializer.db import DeclBase, engine
from app.initializer.logger import logger


def setup():
    # 创建数据库表
    try:
        DeclBase.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully.")
    except Exception as e:
        logger.error(f"Failed to create database tables: {e}")
