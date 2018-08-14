#PythonDraw.py
import turtle
turtle.setup(1600,800,40,40)#设置窗口的大小，位置(width,height,startx,starty),非必须函数，手两者省略为中心位置
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(1)
turtle.pencolor("blue")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
#turtle.done()
