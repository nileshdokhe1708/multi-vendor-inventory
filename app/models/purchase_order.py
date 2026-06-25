from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String
)

from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.base_model import TimestampMixin


class PurchaseOrder(Base, TimestampMixin):

    __tablename__ = "purchase_orders"

    id = Column(
        Integer,
        primary_key=True
    )

    item_id = Column(
        Integer,
        ForeignKey("items.id"),
        nullable=False
    )

    vendor_id = Column(
        Integer,
        ForeignKey("vendors.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    status = Column(
        String(20),
        default="CREATED"
    )

    item = relationship("Item")

    vendor = relationship("Vendor")