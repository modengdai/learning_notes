#文本进度条.py
import time
scale=10
print("开始".center(scale,"="))
start=time.perf_counter()
for i in range(scale+1):
    a="*"*i
    b="."*(scale-i)
    c=i/scale*100
    time.sleep(1)
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.0f}s".format(c,a,b,dur),end="")
time.sleep(1)
print("结束".center(scale,"="))
print("22as24x142")
time.sleep(1)
