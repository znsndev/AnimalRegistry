from .Pet import Pet

class Cat(Pet):
	"""docstring for Cat"""
	def __init__(self, name:str, age:int, birthday:str):
		super().__init__(name, age, birthday)


	def get_commands(self):
		return "Cat cannot follow commands"

	def new_command(self, command):
		return "Cat can't learn commands"
