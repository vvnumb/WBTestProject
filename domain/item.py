from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
	"""Домен тестового задания"""
	value: int
	id: Optional[int] = None  # можно не создавать в домене, вообще может быть value object

	def to_special_dict(self) -> dict:
		# note: вообще, это не задача домена, но не хочу подключать доп. библиотеки
		# и это максимально "удобное" место для данной операции
		return {"id": self.id, "data": {"value": self.value}}
