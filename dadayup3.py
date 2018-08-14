N=input()
N=eval(N)*0.001
a=1
up=(a+N)**365
down=(a-N)**365
print("{:.2f},{:.2f},{:.0f}".format(up,down,int(up/down)))

print("12,3".split(","))
