from fastapi import FastAPI

from app.account.routers import router as account_router
from app.product.routers.category import router as category_router
from app.product.routers.proudct import router as product_router
from app.cart.routers import router as cart_router
from app.shipping.routers import router as shipping_router
app = FastAPI(title="FastApit E-Commerce Backend")


# @app.get("/")
# async def Mehotd():
#     return {"Message ": "This is akshay thigale"}


# @app.get("/school")
# async def Mehotd():
#     return {"Message ": "My school is New English Shool,Tilak Road Pune 30"}


app.include_router(account_router, prefix="/api/account", tags=["Account"])
app.include_router(product_router, prefix="/api/products", tags=["Products"])
app.include_router(category_router, prefix="/api/products-category", tags=["Product Categories"])
app.include_router(cart_router, prefix="/api/carts", tags=["Carts"])
app.include_router(shipping_router, prefix="/api/shippings", tags=["Shippings"])