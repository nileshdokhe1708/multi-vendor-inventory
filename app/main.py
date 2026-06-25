from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
from app.models import *
Base.metadata.create_all(bind=engine)
from app.api.item_routes import router as item_router
from app.api.vendor_routes import router as vendor_router
from app.api.item_vendor_routes import (
    router as item_vendor_router
)
from app.api.order_routes import (
    router as order_router
)
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(item_router)
app.include_router(vendor_router)
app.include_router(item_vendor_router)
app.include_router(order_router)

@app.get("/")
def health_check():
    return {
        "message": "Multi Vendor Inventory System Running"
    }