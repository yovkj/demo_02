from pydantic import BaseModel, Field
from .models import User
class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=5, max_length=16, description="用户名")
    password: str = Field(..., min_length=5, max_length=16, description="密码")

class CommonResponse(BaseModel):
    code: int
    message: str | None = None
    data: dict | None = None

    def dict(self, **kwargs):
        return super().dict(exclude_unset=True, **kwargs)

class LoginRequest(BaseModel):
    username: str = Field(..., min_length=5, max_length=16, description="用户名")
    password: str = Field(..., min_length=5, max_length=16, description="密码")

class LoginResponse(BaseModel):
    code: int
    message: str | None = None
    data: str | None = Field(None, description="JWT令牌")