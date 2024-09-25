from database import Base
from typing import Optional
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date


class Product(Base):

    __tablename__ = "pro"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(16))
    category: Mapped[str] = mapped_column(String(16))
    price: Mapped[int] = mapped_column(Integer, default=0)
    description: Mapped[Optional[str]]
    date: Mapped[date]
    active: Mapped[bool]
