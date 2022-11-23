from turtle import *

def eye():

    begin_fill()
    pendown()
    circle(25)
    end_fill()
    begin_fill()
    color("black")
    circle(10)
    end_fill()
    color("white")



begin_fill()
color("#e6b800")
speed(5)
circle(100)
end_fill()

color("white")
penup()
left(90)
forward(100)
left(90)
forward(50)
left(180)


eye()

penup()
forward(100)

eye()

color("brown")
penup()
left(180)
forward(50)
left(90)
forward(30)
right(90)

eye()

done()