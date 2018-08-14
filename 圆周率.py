#圆周率
from random import random
from time import perf_counter
k=0
c=10*100*10
start=perf_counter()
for i in range(c):
        x,y=random(),random()
        if x**2+y**2<=1:
            k+=1
duration=perf_counter()-start
print(1e2)
print(c,"次的圆周率的值为",k/c*4,"用时{:.2f}".format(duration))

