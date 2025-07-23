# api/src/schemas.py

from pydantic import BaseModel, ConfigDict, PositiveInt, PositiveFloat, condecimal, constr, Field

class Schema(BaseModel):
    """Base schema with config for alias support (camelCase)."""
    model_config = ConfigDict(populate_by_name=True)

class ProductIn(Schema):
    """Product input for shipping request."""
    product_id: PositiveInt = Field(..., alias='productId')
    price: condecimal(gt=0)
    quantity: PositiveInt
    discount: condecimal(ge=0)

class CustomerData(Schema):
    """Customer shipping address and contact information."""
    name: constr(min_length=3)
    shipping_street: str
    commune: str
    phone: constr(pattern=r'^\+\d{8,15}$')

class CartRequest(Schema):
    """Request structure for creating a shipping quote."""
    products: list[ProductIn]
    customer_data: CustomerData

class QuoteOut(Schema):
    """Minimal courier response with the best quote."""
    courier: str
    price: PositiveFloat
