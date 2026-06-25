from app.exceptions.custom_exceptions import VendorNotFoundException, ItemNotFoundException, VendorItemMappingException
from app.models.purchase_order import PurchaseOrder

from app.repositories.order_repository import (OrderRepository)

from app.repositories.item_repository import (ItemRepository)

from app.repositories.vendor_repository import (VendorRepository)

from app.repositories.item_vendor_repository import (ItemVendorRepository)

from app.schemas.purchase_order_schema import (PurchaseOrderCreate)


class OrderService:

    def __init__(
            self,
            order_repository: OrderRepository,
            item_repository: ItemRepository,
            vendor_repository: VendorRepository,
            mapping_repository: ItemVendorRepository
    ):

        self.order_repository = order_repository
        self.item_repository = item_repository
        self.vendor_repository = vendor_repository
        self.mapping_repository = mapping_repository

    def create_order(
            self,
            order_data: PurchaseOrderCreate
    ):

        item = self.item_repository.get_by_id(
            order_data.item_id
        )

        if not item:
            raise ItemNotFoundException(
                "Item not found"
            )

        vendor = self.vendor_repository.get_by_id(
            order_data.vendor_id
        )

        if not vendor:
            raise VendorNotFoundException(
                "Vendor not found"
            )

        mapping = (
            self.mapping_repository.get_vendor_mapping(
                order_data.item_id,
                order_data.vendor_id
            )
        )

        if not mapping:
            raise VendorItemMappingException(
                "Vendor not linked with item"
            )

        order = PurchaseOrder(
            item_id=order_data.item_id,
            vendor_id=order_data.vendor_id,
            quantity=order_data.quantity
        )

        return self.order_repository.create(order)