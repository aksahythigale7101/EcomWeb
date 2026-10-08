from datetime import datetime
from pydantic import BaseModel



class ShippingAddressBase(BaseModel):
    name: str
    address_line1: str
    address_line2: str | None = None
    city: str
    state: str
    pin_code: str
    country: str

class ShippingAddressCreate(ShippingAddressBase):
    pass

class ShippingAddressUpdate(BaseModel):
    name: str | None = None
    address_line1: str | None = None
    address_line2: str | None = None
    city: str | None = None
    state: str | None = None
    pin_code: str | None = None
    country: str | None = None

class ShippingAddressOut(ShippingAddressBase):
    id: int
    user_id: int
    model_config = {"from_attributes": True}

