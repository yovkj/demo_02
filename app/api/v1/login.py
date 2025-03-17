from fastapi import APIRouter, HTTPException
from app.datatype.response import LoginRequest, LoginResponse
from app.business.login import verify_user, create_access_token

router = APIRouter()

@router.post("/user/login", response_model=LoginResponse)
def login(request: LoginRequest):
    is_verify = verify_user(request.username, request.password)
    if is_verify:
        access_token = create_access_token({"sub": request.username})
        return LoginResponse(code=0, message="操作成功", data=access_token)
    raise HTTPException(status_code=400, detail="用户名或密码错误")