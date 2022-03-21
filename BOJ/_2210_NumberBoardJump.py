dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


board = [list(map(int, input().split())) for _ in range(5)]


numlist = []

def dfs(x, y, sum_, L):

     if L == 6:
          if sum_ not in numlist:
               numlist.append(sum_);
          return

     for i in range(4):
          x2 = x + dx[i]
          y2 = y + dy[i]
          
          if 0<=x2<5 and 0<=y2<5:
               dfs(x2, y2, sum_* 10 + board[x][y], L + 1)


for i in range(5):
     for j in range(5):
          dfs(i, j, 0, 0)


print(len(numlist))
     

     
     
