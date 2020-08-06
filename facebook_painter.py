#With little work this code can be optimized to have time complexity O(nk) and space complexity O(1)

def least(n,k,m):
  a=[]
  b=[]
  c=[]
  arr=[]
  for i in range(0,k):
    arr.append((i,m[0][i]))
  arr.sort(key = lambda x: x[1])
  a.append(arr[0])
  b.append(arr[1])
  c.append(arr[2])
  for i in range(1,n):
    arr=[]
    for j in range(0,k):
      arr.append((j,m[i][j]))
    arr.sort(key = lambda x: x[1])
    test=[]
    test.append(a[i-1])
    test.append(b[i-1])
    test.append(c[i-1])
    test.sort(key = lambda x: x[1])
    #a work
    min_color=arr[0][0]
    gal=0
    for i in test:
      if(i[0]!=min_color):
        gal=i[1]
        break
    a.append((min_color,gal+arr[0][1]))

    #b work
    min_color=arr[1][0]
    gal=0
    for i in test:
      if(i[0]!=min_color):
        gal=i[1]
        break
    b.append((min_color,gal+arr[1][1]))

    # c work
    min_color=arr[2][0]
    gal=0
    for i in test:
      if(i[0]!=min_color):
        gal=i[1]
        break
    c.append((min_color,gal+arr[2][1]))
  print(min(a[n-1][1],b[n-1][1],c[n-1][1]))


cost_mat=[[63, 61, 242, 92, 206, 111, 112],
[72, 90, 245, 198, 128, 0, 117],
[210, 174, 188, 95, 113, 56, 179],
[100, 57, 177, 75, 24, 6, 68],
[241, 117, 148, 221, 149, 90, 189],
[89, 211, 120, 62, 139, 165, 95],
[75, 35, 85, 16, 52, 186, 42],
[98, 82, 152, 232, 7, 30, 47],
[27, 20, 76, 206, 83, 102, 110],
[242, 76, 170, 133, 26, 228, 44],
[98, 69, 38, 36, 90, 113, 7],
[128, 99, 40, 236, 27, 110, 1]]



least(len(cost_mat),len(cost_mat[0]),cost_mat)
