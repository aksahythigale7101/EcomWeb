
from ctypes import cast
from sqlalchemy import select
import time
from turtle import ht, st
import uuid
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta, datetime, timezone, tzinfo
from decouple import config
from jose import ExpiredSignatureError, JWTError, jwt
from sqlalchemy.sql.functions import user
from app.account.models import User, RefreshToken

JWT_SECRET_KEY = config("JWT_SECRET_KEY")
JWT_ALGORITHM = config("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_TIME_MIN = config("JWT_ACCESS_TOKEN_TIME_MIN", cast=int)
JWT_REFRESH_TOKEN_TIME_DAY = config("JWT_REFRESH_TOKEN_TIME_DAY", cast=int)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expire_delte: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expire_delte or timedelta(minutes=JWT_ACCESS_TOKEN_TIME_MIN)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)


async def create_token(session: AsyncSession, user: User):
    access_token = create_access_token(data={"sub": str(user.id)})
    refresh_token_str = str(uuid.uuid4())
    expires_at = datetime.now(timezone.utc) + timedelta(
        days=JWT_REFRESH_TOKEN_TIME_DAY
    )

    refresh_token = RefreshToken(
        user_id=user.id, token=refresh_token_str, expires_at=expires_at
    )
    session.add(refresh_token)
    await session.commit()
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }



def decode_token(token:str):
    try:
        return jwt.decode(token,JWT_SECRET_KEY,algorithms=JWT_ALGORITHM)
    except ExpiredSignatureError:
        raise HTTPException(status_code=401,detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid Token")

async def verify_refresh_token(session:AsyncSession,token:str):
    stmt=select(RefreshToken).where(RefreshToken.token == token)
    result =await session.scalars(stmt)
    db_refresh_token= result.first()

    if db_refresh_token and not db_refresh_token.revokrd:
        expire_at= db_refresh_token.expires_at
        if expire_at.tzinfo in None:
            expire_at=expire_at.replace(tzinfo=timezone.utc)
        if expire_at >datetime.now(timezone.utc):
            user_stmt=select(User).where(User.id==db_refresh_token.user_id)
            user_result =await session.scalars(user_stmt)
            return user_result.first()
    return None

