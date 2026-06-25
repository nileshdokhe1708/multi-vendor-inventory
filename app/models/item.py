from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.base_model import TimestampMixin


class Item(Base, TimestampMixin):

    __tablename__ = "items"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(100),
        nullable=False,
        unique=True
    )

    description = Column(
        String(500),
        nullable=True
    )

    stock_quantity = Column(
        Integer,
        default=0
    )

    vendors = relationship(
        "Vendor",
        secondary="item_vendor",
        back_populates="items"
    )