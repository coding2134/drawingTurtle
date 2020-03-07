'''
Created on Mar 7, 2020

@author: ITAUser
'''
import turtle 

spiral = turtle.Turtle()

painter = turtle.Turtle()

painter.pencolor("red")

for i in range(50):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.done()