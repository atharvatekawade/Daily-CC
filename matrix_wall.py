def valid(curr,m):
  if(curr[0]>=0 and curr[1]>=0 and curr[0]<len(m) and curr[1]<len(m[0]) and m[curr[0]][curr[1]]==1):
    return 1
  return 0

def bfs(start,end,m):
  moves=[(0,1),(0,-1),(1,0),(-1,0)]
  queue = []
  visited=[]
  for i in range(0,len(m)):
    visited.append([0]*len(m[0]))
  visited[start[0]][start[1]]=1
  queue.append((start,0))
  flag=0
  while(len(queue)>0 and flag==0):
    #print(queue)
    curr=queue.pop(0)
    for i in moves:
      new=(curr[0][0]+i[0],curr[0][1]+i[1])
      #print(visited)
      if(valid(new,m)==1 and visited[new[0]][new[1]]==0):
        queue.append((new,curr[1]+1))
        visited[new[0]][new[1]]=1
        if(new==end):
          print(curr[1]+1)
          flag=1
          break
  if(flag==0):
    print('No path possible')

mat=[[1,1,1,1],[0,0,1,0],[1,1,1,1],[1,1,1,1]]

bfs((3,0),(0,0),mat)