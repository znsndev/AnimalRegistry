class Animal():
	"""docstring for Animal"""
	def __init__(self, name:str, age:int, birthday:str):
		self.name = name
		self.age = age
		self.birthday = birthday

	def get_name(self) -> str:
		return self.name

	def get_age(self) -> int:
		return self.age

	def get_birthday(self) -> str:
		return self.birthday

	def set_name(self, new_name:str):
		self.name = new_name