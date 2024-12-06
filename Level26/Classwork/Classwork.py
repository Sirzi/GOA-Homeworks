from turtle import *
def walk():
    forward(200)
    left(90)
    forward(100)
    
def fallback():
    forward(-100)
    right(90)
    forward(-200)


walk()
fallback()
exitonclick()