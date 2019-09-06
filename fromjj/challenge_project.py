import turtle
import webbrowser
import time
import numpy

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    some_turtle.circle(100)

def draw_circle2(some_turtle):
    some_turtle.circle(125)

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(250)
        some_turtle.right(120)

def draw_art():

    # time.sleep(10)
    #
    # webbrowser.open("https://www.youtube.com/watch?v=BVRnLUMeAoQ&list=PLmIAixrHzxnbZqAuPGHv4Vy5SosvlfxQv")
    # time.sleep(5)

    window = turtle.Screen()
    window.bgcolor("white")
    tt = turtle.Turtle()
    tt.shape("turtle")
    tt.color("blue")
    tt.speed(15)
# ---------------------------------------------------------------------------------------------
    tt.penup()
    tt.goto(-250,-250)
    tt.pendown()
    length = 360
    j = 1.5
    for i in range(3):
        tt.forward(length)
        tt.left(120)
    i = j*6
    for g in range(180):
        tt.forward(i)
        tt.left(j)
        length = length-j*i
        tt.forward(length)
        length = length-j
        # if i > 0:
        #     length = length-j*i
        #     tt.forward(length)
        #     length = length-j
        # else:
        #     length = length+j*i
        #     tt.forward(length)
        #     length = length - j
        for k in range(2):
            tt.left(120)
            tt.forward(length)
        tt.left(120)
        i = i-0.2

    window.exitonclick()

draw_art()
