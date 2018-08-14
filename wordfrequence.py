#wordfrequence
def gettxt():
    txt=open("harmlet.txt","r").read()
    txt=txt.lower()
    for punctuation in '!"#$%&()*+,-./:;<=>?@[\\]^_‘\'{|}~':
        txt=txt.replace(punctuation," ")
    return txt
hamlettxt=gettxt()
print(hamlettxt)
words=hamlettxt.split()

counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    a,b=items[i]
    print("{:<10}{:>5}".format(a,b))
    


