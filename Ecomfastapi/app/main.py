from fastapi import FastAPI

from app.account.routers import router as account_router

app = FastAPI(title="FastApit E-Commerce Backend")


# @app.get("/")
# async def Mehotd():
#     return {"Message ": "This is akshay thigale"}


# @app.get("/school")
# async def Mehotd():
#     return {"Message ": "My school is New English Shool,Tilak Road Pune 30"}


app.include_router(account_router, prefix="/api/account", tags=["Account"])
