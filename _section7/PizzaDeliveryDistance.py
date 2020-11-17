def dfs(L,s):
     global res

     if L==m:
          total=0
          
          for i in range(len(hs)):
               x1,y1=hs[i]
               dis=2*n
               for j in cb:
                    x2,y2=pz[j]
                    dis=min(dis,abs(x1-x2)+abs(y1-y2))
               total+=dis

          if total<res:
               res=total

                    

     else:
          for i in range(s,len(pz)):
               cb[L]=i
               dfs(L+1,i+1)




if __name__=='__main__':

     n,m=map(int,input().split())
     board=[list(map(int,input().split())) for _ in range(n)]
     res=n*n*n

     hs,pz,cb=[],[],[0]*m


     for i in range(n):
          for j in range(n):
               if board[i][j]==1:
                    hs.append((i,j))
               if board[i][j]==2:
                    pz.append((i,j))

     dfs(0,0)
     print(res)

     
               


'''


import sys

def bfs(x,y,n,board):

     dx=[0,1,0,-1]
     dy=[1,0,-1,0]
     

     res=[[-1]*n for _ in range(n)]
     total_dist=0

     Q=[(x,y)]

     res[x][y]=0

     while Q:
          x_,y_=Q.pop(0)

          for i in range(4):
               xx=x_+dx[i]
               yy=y_+dy[i]

               if 0<=xx<n and 0<=yy<n and res[xx][yy]==-1:
                    Q.append((xx,yy))
                    res[xx][yy]=res[x_][y_]+1

                    if board[xx][yy]==1:
                         total_dist+=res[xx][yy]

          for r in res:
               print(r)
          print()

     return total_dist


n,m=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]

min_dist=n*n*n

for i in range(n):
     for j in range(n):
          if board[i][j]==2:
               temp=bfs(i,j,n,board)
               print(temp)
               print('-----------')
               if temp<min_dist:
                    min_dist=temp

print(min_dist)

               
'''
          
