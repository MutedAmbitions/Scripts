import turtle

pen = turtle.Turtle()
pen.color('red', 'yellow')
pen.begin_fill()
for i in range(50):
    pen.forward(300)
    pen.left(170)
pen.end_fill()
turtle.done()