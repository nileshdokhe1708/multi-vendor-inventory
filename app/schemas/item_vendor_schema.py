from pydantic import BaseModel


class ItemVendorCreate(BaseModel):
    item_id: int
    vendor_id: int