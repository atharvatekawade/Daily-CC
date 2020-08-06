arr=['bed', 'bath', 'bedbath', 'and', 'beyond']
max_len=0
for i in arr:
  if(len(i)>max_len):
    max_len=len(i)
s=set()
for i in arr:
  s.add(i)
dp=[[]]
string='bedbathandbeyond'
n=len(string)
if(string[0:1] in s):
  dp[0].append(string[0:1])
for i in range(1,n):
  if(string[0:i+1] in s):
    dp.append([])
    dp[i].append(string[0:i+1])
  elif(i>max_len):
    flag=0
    for j in range(i,i-max_len,-1):
      if(dp[j-1]!=[] and string[j:i+1] in s):
        dp.append(dp[j-1])
        dp[i].append(string[j:i+1])
        flag=1
        break
    if(flag==0):
      dp.append([])
  else:
    flag=0
    for j in range(i,0,-1):
      if(dp[j-1]!=[] and string[j:i+1] in s):
        dp.append(dp[j-1])
        dp[i].append(string[j:i+1])
        flag=1
        break
    if(flag==0):
      dp.append([])
if(dp[n-1]==[]):
  print('No word break possible')
else:
  print(dp[n-1])

      


