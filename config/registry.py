from infrastructure.item_repository import FileDBItemRepository
from config import settings
from services.get_list_items import GetListItemService
from services.get_single_item import GetSingleItemService
from services.save_new_item import SaveItemService


class Registry:
	@staticmethod
	def get_item_repository():
		return FileDBItemRepository(settings.DB_FILENAME)
	
	@staticmethod
	def get_single_item_service():
		return GetSingleItemService(Registry.get_item_repository())
	
	@staticmethod
	def get_list_item_service():
		return GetListItemService(Registry.get_item_repository())
	
	@staticmethod
	def save_item_service():
		return SaveItemService(Registry.get_item_repository())
