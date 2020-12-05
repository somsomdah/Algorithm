
'''Bottom-Up'''
'''
n=int(input())

d=[0]*(n+1)

d[1]=1
d[2]=2

for i in range(3,n+1):
     d[i]=d[i-1]+d[i-2]

print(d[n])
'''

'''Top-Down'''

n=int(input())
d=[0]*(n+1)

def dfs(l):
     if d[l]>0:
          return d[l]
     if l==1 or l==2:
          return l
     else:
          d[l]=dfs(l-1)+dfs(l-2)
          return d[l]

print(dfs(n))
