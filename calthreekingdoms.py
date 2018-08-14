#calthreekingdoms
import jieba

txt=open("threekingdoms.txt","r",encoding='ANSI').read()
txt=jieba.lcut(txt)

counts={}
exword=('却说','二人','不可','荆州','不能','如此','商议','如何','军士','左右','引兵')
#for word in
for word in txt:
    if len(word)==1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
for word in exword:
    del counts[word]
    
counts=list(counts.items())

    
counts.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    a,b=counts[i]
    print("{:<5}{:>5}".format(a,b))
