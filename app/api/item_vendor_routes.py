from fastapi import APIRouter, Depends

from app.services.item_vendor_service import (
    ItemVendorService
)

from app.dependencies.service_dependencies import (
    get_item_vendor_service
)

router = APIRouter(
    prefix="/item-vendor",
    tags=["Item Vendor"]
)

@router.post("/link")
def link_vendor_to_item(
        item_id: int,
        vendor_id: int,
        service: ItemVendorService = Depends(
            get_item_vendor_service
        )
):
    return service.link_vendor_to_item(
        item_id,
        vendor_id
    )