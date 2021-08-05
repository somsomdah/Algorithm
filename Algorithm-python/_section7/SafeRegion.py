import sys
sys.setrecursionlimit(10000)
#sys.setrecursionlimit()

dx=[-1,0,1,0]
dy=[0,1,0,-1]


n=int(input())
board=[list(int(i) for i in input().split()) for _ in range(n)]

heights=[0]

for row in board:
     heights.extend(row)

heights=list(set(heights))
heights.sort()


def get_checklist(n): # 안전 영역만 남기고 모두 0으로 바꿈
     check=[[int(n<r) for r in row] for row in board]
     return check


checklist=[[0]*n for _ in range(n)]

def dfs(x,y):
     checklist[x][y]=0

     for i in range(4):
               xx=x+dx[i]
               yy=y+dy[i]

               if 0<=xx<n and 0<=yy<n and checklist[xx][yy]==1:
                    dfs(xx,yy)
     
res=-1

for h in heights:
     count=0
     checklist=get_checklist(h)

     for i in range(n):
          for j in range(n):
               if checklist[i][j]==1:
                    dfs(i,j)
                    count+=1

     if count>res:
          res=count

print(res)
     
          
          

     
     
     

               
