from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.dependency import get_db

from app.repositories.item_repository import ItemRepository
from app.repositories.vendor_repository import VendorRepository
from app.repositories.order_repository import OrderRepository
from app.repositories.item_vendor_repository import ItemVendorRepository

from app.services.item_service import ItemService
from app.services.vendor_service import VendorService
from app.services.order_service import OrderService
from app.services.item_vendor_service import ItemVendorService

def get_item_service(
        db: Session = Depends(get_db)
):

    repository = ItemRepository(db)

    return ItemService(repository)

def get_vendor_service(
        db: Session = Depends(get_db)
):

    repository = VendorRepository(db)

    return VendorService(repository)

def get_item_vendor_service(
        db: Session = Depends(get_db)
):

    return ItemVendorService(
        ItemRepository(db),
        VendorRepository(db),
        ItemVendorRepository(db)
    )

def get_order_service(
        db: Session = Depends(get_db)
):

    return OrderService(
        OrderRepository(db),
        ItemRepository(db),
        VendorRepository(db),
        ItemVendorRepository(db)
    )