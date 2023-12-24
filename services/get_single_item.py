from domain.item_repository import ItemRepository


class GetSingleItemService:
	def __init__(self, item_repo: ItemRepository):
		self.item_repo = item_repo
	
	def __call__(self, id: int) -> dict:
		"""Возвращаем словарь как из ТЗ"""
		item = self.item_repo.get_item(id)
		if not item:
			raise ValueError("Данных не обнаружено")
		
		return item.to_special_dict()
