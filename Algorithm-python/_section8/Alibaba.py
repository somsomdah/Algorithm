
n=int(input())

board=[list(map(int,input().split())) for _ in range(n)]
D=[[0]*n for _ in range(n)]
D[0][0]=board[0][0]

for i in range(1,n):
     D[0][i]+=D[0][i-1]+board[0][i]
     D[i][0]+=D[i-1][0]+board[i][0]

for i in range(1,n):
     for j in range(1,n):
          D[i][j]=min(D[i-1][j],D[i][j-1])+board[i][j]

print(D[n-1][n-1])



D=[[0]*n for _ in range(n)]
D[0][0]=board[0][0]

def dfs(x,y):
     
     if D[x][y]>0:
          return D[x][y]
     
     if x==0 and y==0:
          return board[0][0]
     else:
          if y==0:
               D[x][y]= dfs(x-1,y)+board[x][y]
          elif x==0:
               D[x][y]= dfs(x,y-1)+board[x][y]
          else:
               D[x][y] = min(dfs(x,y-1),dfs(x-1,y))+board[x][y]
          return D[x][y]

print(dfs(n-1,n-1))
