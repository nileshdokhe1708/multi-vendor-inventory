from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.base_model import TimestampMixin


class Vendor(Base, TimestampMixin):

    __tablename__ = "vendors"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        nullable=False,
        unique=True
    )

    phone = Column(
        String(20),
        nullable=True
    )

    items = relationship(
        "Item",
        secondary="item_vendor",
        back_populates="vendors"
    )