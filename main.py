# from random import randint
# from turtle import Turtle, Screen
# a = randint(1, 10)
# #print(type(a))
#
# timmy = Turtle()
# #print(timmy)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100.6)
#
# my_screen = Screen()
# #my_screen.canvheight = 500
# #print(my_screen.canvheight)

#my_screen.exitonclick()

from prettytable import PrettyTable

my_table = PrettyTable()
my_table.title = "TITLE"
my_table.add_column("Seoul", ["nowon", "gangnam", "seo"], "l", "t")
my_table.add_column("Seoul2", ["nowon2", "gangnam2", "seo2"], align="r")
my_table.border = True
#my_table.align = "r"
print(my_table.align)
print(my_table)

