from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, HTTPException


def register_middlewares(app: FastAPI):
    # 跨域资源共享中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


async def token_verification_middleware(request: Request, call_next):
    # 从请求头获取令牌
    token = request.headers.get("Authorization")
    if token:
        token = token.replace("Bearer ", "")  # 去除 Bearer 前缀
    if not token:
        raise HTTPException(status_code=401, detail="令牌缺失")
    response = await call_next(request)
    return response


