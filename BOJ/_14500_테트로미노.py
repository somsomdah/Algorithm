import sys

n, m = map(int,input().split()[:2])

board = [list(map(int, sys.stdin.readline().split()[:m])) for _ in range(n)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

res = 0

def dfs(L, x, y, total):
     
     
     check[x][y] = 1
     
     global res
     
     
     if L >= 4:
          res = max(res, total)
          return
     
     for i in range(4):
          xx = x + dx[i]
          yy = y + dy[i]
          if 0<=xx<n and 0<=yy<m and check[xx][yy] == 0:
               
               dfs(L+1, x+dx[i], y+dy[i], total + board[x][y])

def f(x, y):

     global res

     nb = []
     
     for i in range(4):
          xx = x + dx[i]
          yy = y + dy[i]
          if 0<=xx<n and 0<=yy<m:
               nb.append(board[xx][yy])

     if len(nb)>=3:
               nb.sort(reverse=True)
               res = max(res, board[x][y] + sum(nb[:3]))
          
          
          

          
     

for i in range(n):
     for j in range(m):
          check = [[0 for _ in range(m)] for _ in range(n)]
          dfs(0, i, j, 0)
          f(i, j)

print(res)
          
