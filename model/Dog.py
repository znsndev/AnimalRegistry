import random
from .Pet import Pet
from .Command import Command

 

class Dog(Pet):
	"""docstring for Dog"""
	def __init__(self, name: str, age: int, birthday: str):
		super().__init__(name, age, birthday)
		self.state = ""
		self.commands = {}

	def learn_command(self, command: Command):
		if command.get_difficulty() <= random.randint(1, 100):
			self.commands[command.get_name()] = command.make

	def get_commands(self):
		for cmd in self.commands:
			print(cmd)

	def make_command(self, command_name:str, *args):
		if self.commands.get(command_name) != None:
			return self.commands[command_name](*args)
		return f"there is no command {command_name}"


	def set_state(self, new_state):
		self.state = new_state

	def get_state(self):
		return self.state
