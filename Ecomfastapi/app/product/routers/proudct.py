from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status, Query
from app.account.models import User
from app.DB.config import SessionDep
from app.product.schemas import  ProductCreate, ProductOut
from app.account.deps import required_admin
from app.product.services import create_product
router = APIRouter()

@router.post("", response_model=ProductOut)
async def product_create(
  session: SessionDep,
  title: str = Form(...),
  description: str | None = Form(None),
  price: float = Form(...), 
  stock_quantity: int = Form(...), 
  category_ids: Annotated[list[int], Form()] = [],
  image_url: UploadFile | None = File(None), 
  admin_user: User = Depends(required_admin)
  ):
  data = ProductCreate(
    title=title,
    description=description,
    price=price,
    stock_quantity=stock_quantity,
    category_ids=category_ids
  )
  return await create_product(session, data, image_url)