from view.Console import Console
from controller.DataBase import DataBase

db = DataBase()
c = Console(db)


run = True

while run:
	c.menu()
	c.make_menu_option()