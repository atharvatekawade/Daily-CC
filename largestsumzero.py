# I am using dictionary here, one can use avl tree/ordered map to meet specific problem requirements
def maxLen(n, arr):
    d={}
    s=0
    size=0
    for i in range(0,n):
        s=s+arr[i]
        if(s==0):
            size=max(size,i+1)
        elif(s in d):
            size=max(size,i-d[s])
        else:
            d[s]=i
    return size
