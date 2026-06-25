from app.models.item import Item
from app.repositories.item_repository import ItemRepository
from app.schemas.item_schema import ItemCreate


class ItemService:

    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def create_item(self, item_data: ItemCreate):

        item = Item(
            name=item_data.name,
            description=item_data.description,
            stock_quantity=item_data.stock_quantity
        )

        return self.repository.create(item)

    def get_item(self, item_id: int):
        return self.repository.get_by_id(item_id)

    def get_all_items(self):
        return self.repository.get_all()