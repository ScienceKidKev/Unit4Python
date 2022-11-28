from turtle import *
from random import randint, choice as rand_choice 



colors=['blue', 'red', 'green', 'orange', 'purple', 'pink']
speed(0)

for i in range(800):
    penup()
    setposition(randint(-200,200),randint(-200,200))
    pendown()

    #color(rand_choice(colors))
    pencolor(rand_choice(colors))
    fillcolor(rand_choice(colors))
    pensize(3)

    begin_fill()
    circle(randint(10,50),steps=randint(4,10),)
    left(90),right(180)
    end_fill()


done()