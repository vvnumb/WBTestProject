from abc import ABCMeta, abstractmethod
from typing import List, Optional

from domain.item import Item


class ItemRepository(metaclass=ABCMeta):
	
	@abstractmethod
	def get_item(self, id_: int) -> Optional[Item]:
		...
	
	@abstractmethod
	def get_items_list(self) -> List[Item]:
		# note: можно докрутить пагинацию, фильтры и тп
		...
	
	@abstractmethod
	def save_item(self, item: Item) -> Item:
		...
