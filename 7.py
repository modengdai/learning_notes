#7段数码管
import turtle as t
import time
def kong():
    t.penup()
    t.fd(5)
def drawline(draw):
    kong()
    t.pendown() if draw else t.penup()
    t.fd(40)
    kong()
    t.right(90)
    
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [1,3,4,5,6,7,8,9,0] else drawline(False)
    drawline(True) if digit in [2,3,5,6,8,9,0] else drawline(False)
    drawline(True) if digit in [2,6,8,0] else drawline(False)
    t.left(90)
    drawline(True) if digit in [4,5,6,8,9,0] else drawline(False)
    drawline(True) if digit in [2,3,5,6,7,8,9,0] else drawline(False)
    drawline(True) if digit in [1,2,3,4,7,8,9,0] else drawline(False)
    t.penup()
    t.left(180)
    t.fd(20)
def drawdate(date):
    for i in date:
        if i=="-":
            t.write("年",font=("Arial",20,"bold"))
            
            t.fd(30)
        elif i=="=":
            t.write("月",font=("Arial",12,"normal"))
            
            t.fd(30)
        elif i=="+":
            t.write("日",font=("Arial",12,"normal"))
          
            t.fd(30)
        elif i==":":
            t.write(":",font=("Arial",12,"normal"))
            
            t.fd(30)
        else:
            drawdigit(eval(i))
        
def main():
    t.setup(10000,200,50,50)
    t.pensize(5)
    t.penup()
    t.hideturtle()
    t.fd(-500)
    date=time.strftime("%Y-%m=%d+%H:%M:%S",time.localtime())
    drawdate(date)
main()

