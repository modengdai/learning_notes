def trim(s):
        a=0
        b=0
        for i in range(len(s)):#计算前面空格数
            if s[i] !=" ":
                
                break
            a=i+1   
        for i in range(1,len(s)):#计算后面空格数
            if s[-i] !=" ":
                break
            b=i
            
        if b==0:
            return s[a:]
        else:
            return s[a:-b]
       
    
char='hello  '   
print(trim(char))

print(trim('hello  ') != 'hello')
print(trim('  hello') != 'hello')
print(trim('  hello  ') != 'hello')
print(trim('  hello  world  ') != 'hello  world')

