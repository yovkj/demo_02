from contextlib import asynccontextmanager
from fastapi import FastAPI
from app import router, middleware
# 从 app.initializer 导入 setup 函数
from app.initializer import setup
from app.initializer.conf import g

# 调用 setup 函数
setup()

@asynccontextmanager
async def lifespan(app_: FastAPI):
    # 应用启动和关闭时的操作
    yield

app = FastAPI(
    title=g.appname,
    version=g.appversion,
    debug=g.debug,
    lifespan=lifespan,
)
router.register_routers(app)
middleware.register_middlewares(app)