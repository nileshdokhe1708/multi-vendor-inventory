from fastapi import APIRouter, Depends

from app.schemas.vendor_schema import (
    VendorCreate,
    VendorResponse
)

from app.services.vendor_service import VendorService

from app.dependencies.service_dependencies import (
    get_vendor_service
)

router = APIRouter(
    prefix="/vendors",
    tags=["Vendors"]
)

@router.post(
    "",
    response_model=VendorResponse
)
def create_vendor(
        vendor: VendorCreate,
        service: VendorService = Depends(
            get_vendor_service
        )
):
    return service.create_vendor(vendor)

@router.get(
    "",
    response_model=list[VendorResponse]
)
def get_vendors(
        service: VendorService = Depends(
            get_vendor_service
        )
):
    return service.get_all_vendors()