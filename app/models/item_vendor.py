from sqlalchemy import Column, Integer, ForeignKey, Boolean

from app.core.database import Base


class ItemVendor(Base):

    __tablename__ = "item_vendor"

    id = Column(Integer, primary_key=True)

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

    approved = Column(
        Boolean,
        default=True
    )