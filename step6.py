import turtle
def draw_la():
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
def draw_tar():
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(100)
def dot():
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
def draw_ji():
    turtle.backward(45)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(135)
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(30)
turtle.pensize(10)
turtle.speed(2)
turtle.shape("turtle")
draw_la()
turtle.penup()
turtle.goto(-50,-150)
turtle.pendown()
draw_tar()
turtle.penup()
turtle.goto(-60,-100)
turtle.pendown()
dot()
turtle.penup()
turtle.goto(-90,-100)
turtle.pendown()
dot()
turtle.penup()
turtle.goto(-250,-160)
turtle.pendown()
draw_ji()
turtle.penup()
turtle.goto(-210,-230)
turtle.pendown()
dot()
turtle.mainloop()    