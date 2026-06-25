from app.models.purchase_order import PurchaseOrder
from app.repositories.base_repository import BaseRepository


class OrderRepository(BaseRepository):

    def create(self, order: PurchaseOrder):
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def get_by_id(self, order_id: int):
        return (
            self.db.query(PurchaseOrder)
            .filter(PurchaseOrder.id == order_id)
            .first()
        )

    def get_all(self):
        return self.db.query(PurchaseOrder).all()