from fastapi import HTTPException, UploadFile, status
from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession
from app.product.utils import generate_slug, save_upload_file
from app.product.models import Product, Category
from app.product.schemas import CategoryCreate, CategoryOut, ProductCreate

from sqlalchemy.orm import selectinload

################# Category ###################
async def create_category(session: AsyncSession, category:CategoryCreate) -> CategoryOut:
  category = Category(name=category.name)
  session.add(category)
  await session.commit()
  await session.refresh(category)
  return category



async def get_all_categories(session: AsyncSession) -> list[CategoryOut]:
  stmt = select(Category)
  result = await session.execute(stmt)
  return result.scalars().all()

async def delete_category(session: AsyncSession, category_id: int) -> bool:
  category = await session.get(Category, category_id)
  if not category:
    return False
  await session.delete(category)
  await session.commit()
  return True

async def create_product(
    session: AsyncSession, 
    data: ProductCreate, 
    image_url: UploadFile | None = None
  ) -> Product:
  if data.stock_quantity < 0:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Stock quantity cannot be negative")
  
  image_path = await save_upload_file(image_url, "images")

  categories = []
  if data.category_ids:
    category_stmt = select(Category).where(Category.id.in_(data.category_ids))
    category_result = await session.execute(category_stmt)
    categories = category_result.scalars().all()
  
  product_dict = data.model_dump(exclude={"category_ids"})
  if not product_dict.get("slug"):
    product_dict["slug"] = generate_slug(product_dict.get("title"))

  new_product = Product(**product_dict, image_url=image_path, categories=categories)
  session.add(new_product)
  await session.commit()
  return new_product