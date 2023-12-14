from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race: Enter a colour: ")
colors = ["red", "blue", "yellow", "orange", "black", "purple"]
all_turtles = []
print(user_bet)

y_position = [-70, -40, -10, 20, 50, 80]


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y =y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle has won the race")

            else:
                print(f"You've lost! The {winning_colour} turtle has won the race")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



ken = Turtle(shape = "turtle")
ken.color(colors[5])
ken.penup()
ken.goto(x =-230,y = -25)

screen.exitonclick()
