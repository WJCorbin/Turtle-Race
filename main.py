import turtle as t
import random as r

y = 125
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race?\nRed, Orange, "
                                                           "Yellow, Green, Blue, Purple\nEnter a color: ")
is_race_on = False
for place in range(6):
    current_turtle = t.Turtle(shape="turtle")
    current_turtle.penup()
    current_turtle.color(colors[place])
    current_turtle.goto(-230, y)
    turtles.append(current_turtle)
    y -= 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Congratulations the {winner} turtle is the winner!!!")
            else:
                print(f"Sorry but the {winner} turtle won. You lost!!!")
        turtle.forward(r.randint(1, 10))

screen.exitonclick()
