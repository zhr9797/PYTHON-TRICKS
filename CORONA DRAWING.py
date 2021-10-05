#this trick to draw corona virus using turtle library in python :
from turtle import *
color('green')
bgcolor('black')
speed(11)
hideturtle()
b = 0
while b < 200 :
    right(b)
    forward(b * 3)
    b = b + 1 

