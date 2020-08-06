#code
from heapq import heapify, heappush, heappop 
def platforms(time,n):
    time.sort(key = lambda x: x[0])
    m=1
    heap = [] 
    heapify(heap) 
    heappush(heap,time[0][1])
    for i in range(1,n):
        m=max(m,len(heap))
        while(len(heap)>0 and heap[0]<=time[i][0]):
            heappop(heap)
        heappush(heap,time[i][1])
        m=max(m,len(heap))
    print(m)
    
platforms([(900,910),(940,1200),(950,1120),(1100,1130),(1500,1900),(1800,2000)],6)