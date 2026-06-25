from pydantic import BaseModel, Field


class PurchaseOrderCreate(BaseModel):
    item_id: int
    vendor_id: int
    quantity: int = Field(..., gt=0)


class PurchaseOrderResponse(BaseModel):
    id: int
    item_id: int
    vendor_id: int
    quantity: int
    status: str

    class Config:
        from_attributes = True