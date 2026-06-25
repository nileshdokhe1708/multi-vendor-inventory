from sqlalchemy.orm import Session

from app.models.item import Item
from app.repositories.base_repository import BaseRepository


class ItemRepository(BaseRepository):

    def create(self, item: Item) -> Item:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get_by_id(self, item_id: int):
        return (
            self.db.query(Item)
            .filter(Item.id == item_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Item).all()

    def delete(self, item: Item):
        self.db.delete(item)
        self.db.commit()