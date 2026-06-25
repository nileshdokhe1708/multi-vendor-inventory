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
from app.exceptions.custom_exceptions import (
    ItemNotFoundException,
    VendorNotFoundException,
    VendorItemMappingException
)

from app.exceptions.handlers import (
    item_not_found_handler,
    vendor_not_found_handler,
    vendor_mapping_handler
)
from app.core import logger

from app.middleware.logging_middleware import (
    log_requests
)
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(item_router)
app.include_router(vendor_router)
app.include_router(item_vendor_router)
app.include_router(order_router)

app.add_exception_handler(
    ItemNotFoundException,
    item_not_found_handler
)

app.add_exception_handler(
    VendorNotFoundException,
    vendor_not_found_handler
)

app.add_exception_handler(
    VendorItemMappingException,
    vendor_mapping_handler
)
app.middleware("http")(log_requests)
@app.get("/")
def health_check():
    return {
        "message": "Multi Vendor Inventory System Running"
    }