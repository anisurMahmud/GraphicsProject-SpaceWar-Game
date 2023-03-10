import turtle
import os
import random
#turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self,shape=spriteshape)
        self.speed(0)#speed of animation
        self.penup() #don't draw yet
        self.color(color)
        #self.fd(0)
        self.goto(startx,starty)
        self.speed = 1
#sprite creations
player = Sprite("triangle","white",0,0)

delay = input("Press enter to finish. >")