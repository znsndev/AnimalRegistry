import os
from controller.DataBase import DataBase
from model.Cat import Cat
from model.Dog import Dog
from model.Hamster import Hamster
from model.Command import Command

class Console():
	def __init__(self, db):
		self.db = db
		self.clear = lambda: os.system('clear')
		self.title = lambda: print('Animal Registry')
		self.input_field = lambda: print('='*20)

	def make_menu_option(self ):
		option = input()
		match option:
			case '1':
				return self.view_pet_list(self.db.get_pets_list())
			case '2':
				self.new_pet()
			case '3':
				self.remove_pet()
			case '4':
				self.get_pet_info()
			case _:
				pass

	def menu(self):
		self.clear()
		self.title()
		print( "1. View pets list\n2. New pet\n3. Remove pet\n4. Get pet info")
		self.input_field()


	def view_pet_list(self, pet_list):
		self.clear()
		self.title()
		for pet in pet_list:
			print(f"pet ID: {pet[0]}\nspecies: {pet[2]}\nname: {pet[1]}\nage: {pet[3]}\nbirthday: {pet[4]}\n")
		print("1. Back")
		self.input_field()
		a = input()

	def new_pet(self,):
		self.clear()
		self.title()
		self.input_field()
		species = input("Which species: ")
		name = input("What is it name: ")
		age = input("How old is it: ")
		birthday = input("When was it born: ")
		
		match species:
			case 'dog':
				self.db.new_pet(Dog(name, age, birthday), 'dog')
			case 'cat':
				self.db.new_pet(Cat(name, age, birthday), 'cat')
			case 'hamster':
				self.db.new_pet(Hamster(name, age, birthday), 'hamster')
			case _:
				pass


	def remove_pet(self):
		self.clear()
		self.title()
		self.input_field()
		pet_id = int(input("Enter pet ID: "))
		self.db.remove_pet(pet_id)

	def get_pet_info(self):
		self.clear()
		self.title()
		self.input_field()
		pet_id = int(input("Enter pet ID: "))

		self.clear()
		self.title()
		pet = self.db.get_pet(pet_id)
		print(f"pet ID: {pet[0]}\nspecies: {pet[2]}\nname: {pet[1]}\nage: {pet[3]}\nbirthday: {pet[4]}\n")

		cmds = self.db.get_pets_command_list(pet_id)
		if cmds != []:
			for cmd in cmds:
				print(cmd[1])
		print("1. Back\n2. Add command")
		self.input_field()
		opt = input()

		self.make_info_option(opt, pet_id)

	def make_info_option(self, option, pet_id):
		match option:
			case '1':
				pass
			case '2':
				self.clear()
				self.title()
				print("1. Speak\n2. Down\n3. Sit\n4. Back")
				self.input_field()
				cmd = int(input())
				if 0 < cmd < 4:
					commands = ['speak', 'down', 'sit']
					self.db.new_command(pet_id, commands[cmd-1])
			case _:
				pass
