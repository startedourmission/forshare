import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"]

t= turtle.Turtle()

 

turtle.bgcolor("black")

t.speed("fast")

t.width(3)

length = 10

 

while length < 1000 :

    t.forward(length)

    t.pencolor(colors[length%6])

    t.right(89)

    length+=5
