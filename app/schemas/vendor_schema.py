from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class VendorCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: Optional[str] = None


class VendorResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]

    class Config:
        from_attributes = True