from pydantic import BaseModel, Field
from .models import User
from typing import Optional

#注册
class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=5, max_length=16, description="用户名")
    password: str = Field(..., min_length=5, max_length=16, description="密码")

class CommonResponse(BaseModel):
    code: int
    message: str | None = None
    data: dict | None = None

    def dict(self, **kwargs):
        return super().dict(exclude_unset=True, **kwargs)
#登录
class LoginRequest(BaseModel):
    username: str = Field(..., min_length=5, max_length=16, description="用户名")
    password: str = Field(..., min_length=5, max_length=16, description="密码")

class LoginResponse(BaseModel):
    code: int
    message: str | None = None
    data: str | None = Field(None, description="JWT令牌")

# 获取用户详细信息
class UserInfoResponse(BaseModel):
    code: int
    message: Optional[str] = None
    data: Optional[dict] = Field(None, description="用户详细信息")