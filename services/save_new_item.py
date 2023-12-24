from domain.item import Item
from domain.item_repository import ItemRepository


class SaveItemService:
	def __init__(self, item_repo: ItemRepository):
		self.item_repo = item_repo
	
	def __call__(self, value: int) -> dict:
		item = Item(value=value)
		return self.item_repo.save_item(item).to_special_dict()
