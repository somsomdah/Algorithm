import sys

n=int(sys.stdin.readline())
grid=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

m=int(sys.stdin.readline())
for _ in range(m):
     r,d,i=map(int,sys.stdin.readline().split())
     if d==1: # 오른쪽으로 회전
          #temp=grid[r-1][i%n:]+grid[r-1][:i%n]
          for _ in range(i):
               grid[r-1].insert(0,grid[r-1].pop())
     if d==0: # 왼쪽으로 회전
          #temp=grid[r-1][(n-i)%n:]+grid[r-1][:(n-i)%n]
          for _ in range(i):
               grid[r-1].append(grid[r-1].pop(0))
     #grid[r-1]=temp


s,e=0,n
res=0
for r in range(n):
     res+=sum(grid[r][s:e])
     #print(e,s)
     if r<n//2:
          e-=1
          s+=1
     if r>=n//2:
          e+=1
          s-=1
          
          

print(res)
