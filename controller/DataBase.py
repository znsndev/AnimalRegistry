import sqlite3



class DataBase:
	def __init__(self):
		self.connect = sqlite3.connect('pets.sqlite')
		self.cursor = self.connect.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS pets(id, name, species, age, birthday)")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS commands(pet_id, command_name)")

	def get_pets_list(self):
		self.cursor.execute("SELECT * FROM pets")
		pets_list = self.cursor.fetchall()
		# self.connect.close()
		return pets_list


	def get_pets_command_list(self, pet_id):
		self.cursor.execute(f"SELECT * FROM commands where pet_id={pet_id}")
		pets_list = self.cursor.fetchall()
		# self.connect.close()
		return pets_list

	def new_pet(self, pet, species):
		self.cursor.execute(f"INSERT INTO pets (id, name, species, age, birthday) VALUES ({self.get_new_pet_id()}, '{pet.get_name()}', '{species}', {pet.get_age()}, '{pet.get_birthday()}')")
		self.connect.commit()

	def new_command(self, pet_id, command_name):
		self.cursor.execute(f"INSERT INTO commands (pet_id, command_name) VALUES ({int(pet_id)}, '{command_name}'")
		self.connect.commit()



	def get_new_pet_id(self):
		req = self.cursor.execute("SELECT * FROM pets")
		answ = req.fetchall()
		return len(answ)+1

	def remove_pet(self, pet_id):
		self.cursor.execute(f"DELETE FROM pets WHERE id = {pet_id}")

	def get_pet(self, pet_id):
		p = self.cursor.execute(f"SELECT * FROM pets WHERE id = {pet_id}")
		# print(p.fetchall())
		p = p.fetchall()[0]
		return p


