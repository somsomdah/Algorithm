import sys
sys.setrecursionlimit(10**7)

dx=[0,1,0,-1]
dy=[-1,0,1,0]



def dfs(x,y):
     global count
     
     board[y][x]=0
     
     for i in range(4):
          xx=x+dx[i]
          yy=y+dy[i]

          if 0<=xx<m and 0<=yy<n and board[yy][xx]==1:
                    dfs(xx,yy)
     


if __name__=="__main__":

     
     t=int(input())

     for _ in range(t):
          m,n,k=map(int,input().split())

          board=[[0]*m for _ in range(n)]

          for _ in range(k):
               x,y=map(int,input().split())
               board[y][x]=1

          count=0
          for i in range(m):
               for j in range(n):
                    if board[j][i]==1:
                         dfs(i,j)
                         count+=1
          
          print(count)
          



