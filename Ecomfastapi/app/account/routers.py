
import re
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from app.account.deps import get_current_user
from app.account.utils import create_token, verify_refresh_token
from app.account.schemas import UserCreate, UserOut, UserLogin
from app.account.services import User, create_user, authenticate_user
from app.DB.config import SessionDep
from fastapi import HTTPException, status

router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register(session: SessionDep, user: UserCreate):
    return await create_user(session, user)


@router.post("/login")
async def login(session: SessionDep, user_login: UserLogin):
    user = await authenticate_user(session, user_login)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
        )

    tokens = await create_token(session, user)
    response = JSONResponse(content={"Message": "Login scuccessful"})
    response.set_cookie(
        "access_token",
        value=tokens["access_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60 * 24 * 1,
    )
    response.set_cookie(
        "refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60 * 24 * 7,
    )
    # return user
    return response


@router.get("/me", response_model=UserOut)
async def me(user: User = Depends(get_current_user)):
    return user


@router.post("/refresh")
async def refresh_token(session: SessionDep, request: Request):
    token = request.cookies.get("refresh_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing refresh_token"
        )

    user = await verify_refresh_token(session, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalied or expired refresh token",
        )
    tokens = await create_token(session, user)
    response = JSONResponse(content={"Message": "Token Refreshed scuccessful"})
    response.set_cookie(
        "access_token",
        value=tokens["access_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60 * 24 * 1,
    )
    response.set_cookie(
        "refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60 * 24 * 7,
    )
    # return user
    return response
