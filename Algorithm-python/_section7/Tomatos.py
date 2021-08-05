
c,r=map(int,input().split()) #columns,rows
board=[[int(e) for e in input().split()] for _ in range(r)]

def bfs(c,r,board):
     dx=[1,0,-1,0]
     dy=[0,1,0,-1]

     des=[[0]*c for _ in range(r)] 
     Q=[]

     for i in range(r):
          for j in range(c):
               if board[i][j]==1:
                    Q.append((i,j))

     while Q:
          x,y=Q.pop(0)
          #print(x,y)

          for i in range(4):
               xx=x+dx[i]
               yy=y+dy[i]

               if 0<=xx<r and 0<=yy<c and board[xx][yy]==0:
                    board[xx][yy]=1
                    des[xx][yy]=des[x][y]+1
                    Q.append((xx,yy))
                         


     max_val=-1
     for i in range(r):
         for j in range(c):
             if board[i][j]==0: #토마토가 익지 않음
                 print(-1)
                 sys.exit(0)
             elif des[i][j]>max_val: # 익은 토마토에 한해 최대값 찾기
                 max_val=des[i][j]

     print(max_val)


bfs(c,r,board)
