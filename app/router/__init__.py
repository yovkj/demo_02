from fastapi import FastAPI
from app.api.v1.user_register import router as user_register_router
from app.api.v1.login import router as login_router  # 新增登录路由导入
def register_routers(app: FastAPI):
    app.include_router(user_register_router, prefix="/api")

def register_routers(app: FastAPI):
    app.include_router(user_register_router, prefix="/api")
    app.include_router(login_router, prefix="/api")  # 注册登录路由