import os

# 基础配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库配置
DB_URL = "sqlite:///./test.db"

# 应用配置
APP_NAME = "FastAPI App"
APP_VERSION = "1.0.0"
DEBUG = True

# config/settings.py 补充内容
SECRET_KEY = "your-secret-key-123456"  # 实际使用强密码，建议从环境变量读取
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

