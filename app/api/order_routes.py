from fastapi import APIRouter, Depends

from app.schemas.purchase_order_schema import (
    PurchaseOrderCreate,
    PurchaseOrderResponse
)

from app.services.order_service import OrderService

from app.dependencies.service_dependencies import (
    get_order_service
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post(
    "",
    response_model=PurchaseOrderResponse
)
def create_order(
        order: PurchaseOrderCreate,
        service: OrderService = Depends(
            get_order_service
        )
):
    return service.create_order(order)