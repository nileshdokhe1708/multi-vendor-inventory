from app.repositories.item_repository import ItemRepository
from app.repositories.vendor_repository import VendorRepository
from app.repositories.item_vendor_repository import (
    ItemVendorRepository
)


class ItemVendorService:

    def __init__(
            self,
            item_repository: ItemRepository,
            vendor_repository: VendorRepository,
            mapping_repository: ItemVendorRepository
    ):
        self.item_repository = item_repository
        self.vendor_repository = vendor_repository
        self.mapping_repository = mapping_repository

    def link_vendor_to_item(
            self,
            item_id: int,
            vendor_id: int
    ):

        item = self.item_repository.get_by_id(item_id)

        if not item:
            raise ValueError("Item not found")

        vendor = self.vendor_repository.get_by_id(vendor_id)

        if not vendor:
            raise ValueError("Vendor not found")

        return self.mapping_repository.create_link(
            item_id,
            vendor_id
        )