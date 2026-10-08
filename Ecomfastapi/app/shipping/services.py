from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.shipping.schemas import ShippingAddressCreate, ShippingAddressOut, ShippingAddressUpdate
from app.shipping.models import ShippingAddress

async def create_shipping_address(
    session: AsyncSession,
    user_id: int,
    data: ShippingAddressCreate
) -> ShippingAddressOut:
  address = ShippingAddress(user_id=user_id, **data.model_dump())
  session.add(address)
  await session.commit()
  await session.refresh(address)
  return address


# SELECT * FROM shipping_address WHERE user_id = :user_id
async def list_user_shipping_addresses(
    session: AsyncSession,
    user_id: int
) -> list[ShippingAddressOut]:
  stmt = select(ShippingAddress).where(ShippingAddress.user_id == user_id)
  result = await session.execute(stmt)
  return result.scalars().all()

# SELECT * FROM shipping_address WHERE id = :address_id
async def get_user_shipping_address_by_address_id(
  session: AsyncSession,
  address_id: int,
  user_id: int
) -> ShippingAddressOut:
  address = await session.get(ShippingAddress, address_id)
  if not address or address.user_id != user_id:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found or not authorized")
  return address

async def update_user_shipping_address_by_address_id(
  session: AsyncSession,
  address_id: int,
  user_id: int,
  data: ShippingAddressUpdate
) -> ShippingAddressOut:
  address = await session.get(ShippingAddress, address_id)
  if not address or address.user_id != user_id:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found or not authorized")
  for key, value in data.model_dump(exclude_unset=True).items():
    setattr(address, key, value)
  await session.commit()
  await session.refresh(address)
  return address


async def delete_shipping_address_by_address_id(
  session: AsyncSession, 
  user_id: int, 
  address_id: int
):
  address = await session.get(ShippingAddress, address_id)
  if not address or address.user_id != user_id:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found or not authorized")
  await session.delete(address)
  await session.commit()
  return {"message": "Address deleted"}
