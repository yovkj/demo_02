# from fastapi import APIRouter, HTTPException, Depends
# from app.datatype.response import UserInfoResponse
# from app.business.login import verify_token  # 需补充JWT验证函数（见下方说明）
# from app.business.user_info import get_user_info
#
# router = APIRouter()
#
# # 补充JWT验证函数（可放在login.py或单独utils）
# from jose import JWTError, jwt
# from app.initializer.conf import g
#
# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, g.SECRET_KEY, algorithms=[g.ALGORITHM])
#         return payload.get("sub")
#     except JWTError:
#         raise HTTPException(status_code=401, detail="无效的令牌")
#
# @router.get("/user/userInfo", response_model=UserInfoResponse)
# def get_user_detail_info(token: str = Depends(verify_token)):
#     username = verify_token(token)
#     user_info = get_user_info(username)
#     if user_info:
#         return UserInfoResponse(code=0, message="操作成功", data=user_info)
#     raise HTTPException(status_code=404, detail="用户信息未找到")


from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.datatype.response import UserInfoResponse
from app.business.login import verify_token
from app.business.user_info import get_user_info
from fastapi import Header  # 新增导入

# router = APIRouter()
#
# # 定义从请求头获取令牌的方式
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)
#
# @router.get("/user/userInfo", response_model=UserInfoResponse)
# def get_user_detail_info(
#     token: str = Header(None)  # 从请求头获取token，修改此处
# ):
#     if not token:
#         raise HTTPException(status_code=401, detail="令牌缺失")
#     username = verify_token(token)
#     user_info = get_user_info(username)
#     if user_info:
#         return UserInfoResponse(code=0, message="操作成功", data=user_info)
#     raise HTTPException(status_code=404, detail="用户信息未找到")
#

from fastapi import Header, HTTPException, Depends
from app.datatype.response import UserInfoResponse
from app.business.login import verify_token
from app.business.user_info import get_user_info

router = APIRouter()

@router.get("/user/userInfo", response_model=UserInfoResponse)
def get_user_detail_info(
    token: str = Header(None)  # 确认此处是 Header，而非 Query
):
    print(f"接收到的 token：{token}")  # 添加打印日志
    if not token:
        raise HTTPException(status_code=401, detail="令牌缺失")
    username = verify_token(token)
    user_info = get_user_info(username)
    if user_info:
        return UserInfoResponse(code=0, message="操作成功", data=user_info)
    raise HTTPException(status_code=404, detail="用户信息未找到")