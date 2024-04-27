class Command():
	"""docstring for Command"""
	def speak():
		return "woof"

	def down(pet):
		if pet.get_state != "lying":
			pet.set_state("lying")
			return f"{pet.get_name()} is lying down now"
		return f"{pet.get_name()} just lies there"

	def sit(pet):
		if pet.get_state != "sitting":
			pet.set_state("sitting")
			return f"{pet.get_name()} is sitting now"
		return f"{pet.get_name()} just sits there"
