def countDistinct(arr,n,k):
    if(k==1):
        return [1]*n
    a=[]
    cnt=0
    d={}
    for i in range(0,k):
        if(arr[i] in d):
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
            cnt+=1
    a.append(cnt)
    for i in range(k,n):
        if(arr[i-k]!=arr[i]):
            d[arr[i-k]]=d[arr[i-k]]-1
            if(d[arr[i-k]]==0):
                cnt=cnt-1
            if(arr[i] in d and d[arr[i]]!=0):
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
                cnt+=1
        a.append(cnt)
    return a