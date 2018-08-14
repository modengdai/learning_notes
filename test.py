lt=[10,8,12,15,17,19,45,75,48,85,56,15,14,2,8]
print(sorted(lt))
n=len(lt)
ls=[]
for i in range(n):
        ls.append(lt.pop(lt.index((max(lt)))))
print(ls)
sorted(lt)
