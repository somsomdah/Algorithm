def solution(m, n, picture):

     a = [[0 for _ in range(n)] for _ in range(m)]
     
     dx = [0, 1, 0, -1]
     dy = [1, 0, -1, 0]

     count = 0
     largest = -1
     temp = 0
     

     def dfs(x, y):

          a[x][y] = 1
          
          nonlocal temp
          temp += 1

          for i in range(4):

               x2 = x + dx[i]
               y2 = y + dy[i]

               if 0<=x2<m and 0<=y2<n and a[x2][y2] == 0:
                    if picture[x][y] == picture[x2][y2]:
                         dfs(x2, y2)

     for i in range(m):
          for j in range(n):
               if a[i][j] == 0 and picture[i][j]>0:
                    print(i,j)
                    dfs(i, j)
                    count += 1
                    largest = max(largest, temp)
                    temp = 0


     return [count, largest]


print(solution(6, 4, [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]))

          
          
          
