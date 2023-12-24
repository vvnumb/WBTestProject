from typing import List, Optional

from domain.item import Item
from domain.item_repository import ItemRepository


class FileDBItemRepository(ItemRepository):
	def __init__(self, db_filename: str):
		self._db_filename = db_filename
		try:
			file = open(self._db_filename, "r+")
		except FileNotFoundError:
			file = open(self._db_filename, "w+")
		finally:
			file.close()
		
	
	def save_item(self, item: Item) -> Item:
		if item.id is not None:
			raise ValueError("Id объекта должен быть проставлен автоматичекски")
		last_pk = 0
		with open(self._db_filename, "r+") as db_file:
			for line in db_file:
				current_item = self._parse_raw_line(line)
				last_pk = max(int(current_item.id), last_pk)
		
		item.id = last_pk + 1
		with open(self._db_filename, "a+") as db_file:
			raw_line = ";".join([str(item.id), str(item.value)])
			raw_line += "\n"
			db_file.write(raw_line)
		return item
	
	def get_item(self, id_: int) -> Optional[Item]:
		# note: если форматирвоать файл так, чтобы каждая строка занимала одинаковое кол-во
		# символов, то можно реализовать бин поиск, O(n) -> O(logn) по вермени
		with open(self._db_filename, "r+") as db_file:
			for line in db_file:
				item = self._parse_raw_line(line)
				if item.id == id_:
					return item
		return None
	
	def get_items_list(self) -> List[Item]:
		items = []
		with open(self._db_filename, "r+") as db_file:
			for line in db_file:
				item = self._parse_raw_line(line)
				items.append(item)
		return items
	
	def _parse_raw_line(self, line: str) -> Item:
		tokens = line.split(";")
		if len(tokens) != 2:
			raise ValueError("Неконсистентная строка в бд: ", line)
		item = Item(id=int(tokens[0]), value=int(tokens[1]))
		return item
