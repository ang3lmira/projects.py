#import turtle
#bubu = turtle.Turtle()

#from turtle import Turtle, Screen
#bubu = Turtle()
# bubu.shape("turtle")
# bubu.color("pink")
# bubu.forward(100)
# print(bubu)

#a_screen = Screen()
# print(a_screen.canvheight)

# a_screen.exitonclick()

from prettytable import PrettyTable
my_table = PrettyTable()

my_table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Obibaby"])
my_table.add_column("Pokemon type", ["Electric", "Water", "Fire"])
my_table.align = "r"
print(my_table)
