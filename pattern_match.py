def encode(word):
    d={}
    curr=0
    s=''
    for i in word:
        if(i not in d):
            curr=curr+1
            d[i]=curr
        s=s+str(d[i])
    return s
        

def findSpecificPattern(Dict, pattern):
    a=encode(pattern)
    arr=[]
    for i in Dict:
        if(a==encode(i)):
            arr.append(i)
    return arr