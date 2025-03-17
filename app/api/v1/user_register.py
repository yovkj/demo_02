from fastapi import APIRouter, HTTPException
from app.datatype.response import UserRegisterRequest, CommonResponse
from app.business.user_register import register_user

router = APIRouter()

@router.post("/user/register", response_model=CommonResponse)
def user_register(request: UserRegisterRequest):
    username = request.username
    password = request.password
    is_success = register_user(username, password)
    if is_success:
        return CommonResponse(code=0, message="注册成功")
    else:
        raise HTTPException(status_code=400, detail="用户名已存在")