import turtle
import os
import random
#turtle.fd(0)
turtle.speed(0)#animation speed
turtle.bgcolor("black")#background color
turtle.hideturtle()
turtle.setundobuffer(1)#saves memory
turtle.tracer(1)#speeds up drawing

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self,shape=spriteshape)
        self.speed(0)#speed of animation
        self.penup() #don't draw yet
        self.color(color)
        #self.fd(0)
        self.goto(startx,starty)
        self.speed = 1
    def move(self):
        self.forward(self.speed)
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3
    def turn_left(self):
        self.left(45)
    def turn_right(self):
        self.right(45)
    def accelerate(self):
        self.speed +=1
    def breaks(self):
        self.speed -=1
#sprite creations
player = Player("triangle","white",0,0)

#keyboard settings
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.breaks,"Down")
turtle.listen()

#game
while True:
    player.move()

delay = input("Press enter to finish. >")