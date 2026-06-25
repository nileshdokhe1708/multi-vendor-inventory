from fastapi import APIRouter, Depends

from app.schemas.item_schema import (
    ItemCreate,
    ItemResponse
)

from app.services.item_service import ItemService

from app.dependencies.service_dependencies import (
    get_item_service
)

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.post(
    "",
    response_model=ItemResponse
)
def create_item(
        item: ItemCreate,
        service: ItemService = Depends(
            get_item_service
        )
):
    return service.create_item(item)

@router.get(
    "",
    response_model=list[ItemResponse]
)
def get_items(
        service: ItemService = Depends(
            get_item_service
        )
):
    return service.get_all_items()