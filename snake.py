import turtle
import time

delay = 0.1

wn = turtle.Screen()
wn.title('snake game')
wn.bgcolor('blue')
wn.setup(width=600, height=600)
wn.tracer(0)

#create head of snake
head = turtle.Turtle
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = 'up'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.directon == 'left':
        x = head.xcor()
        head.sety(x-20)

    if head.direction == 'right':
        x = head.xcor()
        head.sety(x+20)

while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop()

