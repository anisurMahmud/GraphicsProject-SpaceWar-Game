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
        #boundary
        if self.xcor() >290:
            self.setx(290)
            self.right(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.right(60)
        if self.ycor() >290:
            self.sety(290)
            self.right(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.right(60)
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
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3
    def draw_border(self):
        #draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300,300)
        self.pen.pendown()
        for side in range(4):
            self.pen.forward(600)
            self.pen.right(90)
        self.pen.penup()
        self.pen.hideturtle()
#game object
game = Game()
#game border
game.draw_border()

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