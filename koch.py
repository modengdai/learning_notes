
#KochDrawV1.py
import turtle
def koch(n,l):
    if n==0:
        turtle.fd(l)
    else:
        for i in [0,60,-120,60]:
            turtle.left(i)
            koch(n-1,l/3)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pensize(2)
    turtle.pendown()
    level=3
    koch(level,600)
    turtle.right(120)
    koch(level,600)
    turtle.right(120)
    koch(level,600)
    turtle.hideturtle
main()
