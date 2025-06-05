"""
turtle_race.py

Created a fun turtle race game using Python's turtle graphics.

How the game works:
Place a bet by picking a color of the turtle that you think will win.
Once the race starts, the turtles moves forward by random amounts until one crosses the finish line.
If your turtle wins, you win! If not, better luck next time.


- Six colorful turtles line up and race across the screen.
- The race is totally random, so it's anyone's guess who will win.
- Just click the window when you're done to close it.

A great way to play around with turtle graphics, user input, and a bit of friendly competition!
"""


from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")
print(f"Your bet is: {user_bet}")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
