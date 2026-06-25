from app.models.vendor import Vendor
from app.repositories.vendor_repository import VendorRepository
from app.schemas.vendor_schema import VendorCreate


class VendorService:

    def __init__(self, repository: VendorRepository):
        self.repository = repository

    def create_vendor(self, vendor_data: VendorCreate):

        vendor = Vendor(
            name=vendor_data.name,
            email=vendor_data.email,
            phone=vendor_data.phone
        )

        return self.repository.create(vendor)

    def get_vendor(self, vendor_id: int):
        return self.repository.get_by_id(vendor_id)

    def get_all_vendors(self):
        return self.repository.get_all()