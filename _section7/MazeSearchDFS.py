dx=[-1,0,1,0]
dy=[0,1,0,-1]




def dfs(x,y):
     global count
     
     if x==6 and y==6:
          count+=1

     else:
          for i in range(4):
               xx=x+dx[i]
               yy=y+dy[i]

               if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                    # 백트래킹 공식
                    board[xx][yy]=1
                    dfs(xx,yy)
                    board[xx][yy]=0





if __name__=="__main__":

     board=[list(map(int,input().split())) for _ in range(7)]
     board[0][0]=1

     count=0

     dfs(0,0)

     print(count)
