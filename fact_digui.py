def jiecheng(n):
    a=n*jiecheng(n-1)
    
    return a
n=eval(input())
while n>0:
    jiecheng(n)
print(a)
