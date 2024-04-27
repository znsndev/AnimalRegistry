import sys
from .Animal import Animal
sys.path.append('../')
from .Command import Command

class Pet(Animal):
	"""docstring for Pet"""
	def __init__(self, name:str, age:int, birthday:str):
		super().__init__(name, age, birthday)

	def get_commands(self):
		pass

	def new_command(self, command: Command):
		pass


