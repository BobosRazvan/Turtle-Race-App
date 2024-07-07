import turtle
import random
from tkinter import messagebox

screen = turtle.Screen()
screen.bgcolor("white")
is_race_on = False
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []

for index, color in enumerate(colors):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + index * 30)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo(title="Race Result",
                                    message=f"You've won! The {winning_color} turtle is the winner!")
            else:
                messagebox.showinfo(title="Race Result",
                                    message=f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.listen()
screen.exitonclick()
