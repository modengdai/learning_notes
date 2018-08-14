def trim(s):
        a=b=i=0
        j=len(s)
        while i < j:#计算前面空格数
            if s[i] !=" ":
                break
            i+=1
        if i==j-1:
            return "该字符串全为空格"
        a=i    
        i=len(s)-1
        while i >=0:#计算前面空格数
            if s[i] !=" ":
                break
            i-=1
        b=i+1
        return s[a:b]
       
    
char='  hello  '   
print(trim(char))

print(trim('hello  ') != 'hello')
print(trim('  hello') != 'hello')
print(trim('  hello  ') != 'hello')
print(trim('  hello  world  ') != 'hello  world')
