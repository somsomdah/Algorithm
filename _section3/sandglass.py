import sys

n=int(sys.stdin.readline())
grid=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

m=int(sys.stdin.readline())
for _ in range(m):
     r,d,i=map(int,sys.stdin.readline().split())
     if d==1: # 오른쪽으로 회전
          temp=grid[r-1][i%n:]+grid[r-1][:i%n]
     if d==0: # 왼쪽으로 회전
          temp=grid[r-1][(n-i)%n:]+grid[r-1][:(n-i)%n]

     grid[r-1]=temp


s,e=1,n
res=0
for r in range(n):
     print(s,e)
     if s<e
          res+=sum(grid[r][s:e])
     if s>e
          res+=sum(grid[r][e:s])

     s+=1
     e-=1

print(res)
