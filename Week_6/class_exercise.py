from turtle import Screen, Turtle

def triangle(side):
    tess.pendown()

    for _ in range(3):
        tess.forward(side)
        tess.left(120)

    tess.penup()

def sixPtdStar(side):
    height = side * 3**0.5 / 2  # equilateral triangle

    for _ in range(2):
        tess.right(30)
        tess.forward(2 * height / 3)
        tess.left(90 + 60)
        triangle(side)
        tess.right(90 + 60) 
        tess.backward(2 * height / 3)
        tess.right(30)

tess = Turtle()
tess.penup()


sixPtdStar(100)

screen = Screen()
screen.exitonclick()
