from .Pet import Pet

class Hamster(Pet):
	"""docstring for Hamster"""
	def __init__(self, name:str, age:int, birthday:str):
		super().__init__(name, age, birthday)


	def get_commands(self):
		return "Hamster cannot follow commands"

	def new_command(self, command):
		return "Hamster can't learn commands"
