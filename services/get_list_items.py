from typing import List

from domain.item_repository import ItemRepository


class GetListItemService:
	def __init__(self, item_repo: ItemRepository):
		self.item_repo = item_repo
		
	def __call__(self) -> List[dict]:
		items = self.item_repo.get_items_list()
		response = [item.to_special_dict() for item in items]
		return response
