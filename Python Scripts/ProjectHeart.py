import turtle

pen = turtle.Turtle()


def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.pensize(3)
    pen.color('red', '#c6fc03')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(113)
    pen.end_fill()
heart()
turtle.done()