from fastapi import FastAPI
from app.router import register_routers  # 假设路由注册逻辑在此
from app.middleware import register_middlewares  # 假设中间件注册逻辑在此

app = FastAPI()
register_routers(app)  # 注册路由
register_middlewares(app)  # 注册中间件

