dx=[1,0,-1,0]
dy=[0,-1,0,1]


def dfs(x,y):
     #print(x,y)
     global count
     if (x,y)==max_index:
          count+=1
          return
     else:
          for i in range(4):
               xx=x+dx[i]
               yy=y+dy[i]
               #print(board[xx][yy]>board[x][y])

               if 0<=xx<n and 0<=yy<n and board[xx][yy]>board[x][y]:
                    dfs(xx,yy)
          


if __name__=="__main__":

     n=int(input())
     board=[list(map(int,input().split())) for _ in range(n)]
     visited=[[0]*n for _ in range(n)]

     count=0

     min_val=min([min(r) for r in board])
     max_val=max([max(r) for r in board])

     #print(min_val,max_val)

     for i in range(n):
          for j in range(n):
               if board[i][j]==min_val:
                    min_index=(i,j)
                    break

     for i in range(n):
          for j in range(n):
               if board[i][j]==max_val:
                    max_index=(i,j)
                    break

     dfs(min_index[0],min_index[1])
     print(count)



