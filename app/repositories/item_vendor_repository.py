from app.models.item_vendor import ItemVendor
from app.repositories.base_repository import BaseRepository


class ItemVendorRepository(BaseRepository):

    def create_link(
            self,
            item_id: int,
            vendor_id: int
    ):

        link = ItemVendor(
            item_id=item_id,
            vendor_id=vendor_id
        )

        self.db.add(link)
        self.db.commit()
        self.db.refresh(link)

        return link

    def get_vendor_mapping(
            self,
            item_id: int,
            vendor_id: int
    ):

        return (
            self.db.query(ItemVendor)
            .filter(
                ItemVendor.item_id == item_id,
                ItemVendor.vendor_id == vendor_id
            )
            .first()
        )