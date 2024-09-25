from typing import Optional
from pydantic import BaseModel
from datetime import date
# from models import Product

class ProductListValidate(BaseModel):
    product_name: str
    category: str
    price: int
    description: Optional[str] = None
    date: date
    active: bool


