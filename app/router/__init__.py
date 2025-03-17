from fastapi import FastAPI
from app.api.v1.user_register import router as user_register_router
from app.api.v1.login import router as login_router  # 新增登录路由导入
from app.api.v1.user_info import router as user_info_router  # 新增获取路由导入


#获取用户详情
def register_routers(app: FastAPI):
    app.include_router(user_register_router, prefix="/api")
    app.include_router(login_router, prefix="/api")
    app.include_router(user_info_router, prefix="/api")  # 注册新路由