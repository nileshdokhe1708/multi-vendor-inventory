from pydantic import BaseModel, Field
from typing import Optional


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = None
    stock_quantity: int = Field(default=0, ge=0)


class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    stock_quantity: int

    class Config:
        from_attributes = True