from fastapi import APIRouter, Depends, HTTPException, status


from app.order.services import checkout
from app.order.schemas import OrderOut
from app.account.deps import get_current_user
from app.account.models import User
from app.DB.config import SessionDep


from app.payment.schemas import PaymentCreate

router = APIRouter()

@router.post("/checkout", response_model=OrderOut)
async def checkout_order(
    session: SessionDep,
    payment_data: PaymentCreate,
    user: User = Depends(get_current_user)
):
  return await checkout(session, user.id, payment_data)
