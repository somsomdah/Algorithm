dx=[-1,0,1,0,1,-1,-1,1]
dy=[0,1,0,-1,1,1,-1,-1]


n=int(input())
board=[list(int(i) for i in input().split()) for _ in range(n)]



Q=[]
count=0

def bfs(x,y):
     global count
     
     if board[x][y]==1:
          board[x][y]=0
          Q.append((x,y))

     while Q:

          tmpx,tmpy=Q.pop(0)

          for i in range(8):

               xx=tmpx+dx[i]
               yy=tmpy+dy[i]

               if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
                    
                         board[xx][yy]=0
                         Q.append((xx,yy))


     count+=1



for i in range(n):
      for j in range(n):
           if board[i][j]==1:
                bfs(i,j)

print(count)
     
     
