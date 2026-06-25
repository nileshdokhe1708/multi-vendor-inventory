from app.models.vendor import Vendor
from app.repositories.base_repository import BaseRepository


class VendorRepository(BaseRepository):

    def create(self, vendor: Vendor):
        self.db.add(vendor)
        self.db.commit()
        self.db.refresh(vendor)
        return vendor

    def get_by_id(self, vendor_id: int):
        return (
            self.db.query(Vendor)
            .filter(Vendor.id == vendor_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Vendor).all()