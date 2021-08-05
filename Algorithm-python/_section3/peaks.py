import sys

n=int(sys.stdin.readline())
a=[ list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for row in a:
     row.insert(0,0)
     row.append(0)

a.insert(0,[0]*(n+2))
a.append([0]*(n+2))

'''
count=0
for i in range(1,n+1):
     for j in range(1,n+1):
          if (a[i][j]>a[i][j+1] and a[i][j]>a[i][j-1]) and (a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j]):
               count+=1

print(count)
'''

dx=[-1,0,1,0]
dy=[0,1,0,-1]
count=0
for i in range(1,n+1):
     for j in range(1,n+1):
          if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)) : # k에 대해 모두 성립하면
               count+=1

print(count)
