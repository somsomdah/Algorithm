n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    
    if visited[x][y]:
        return
    
    visited[x][y] = 1
    land.append((x, y))

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and l <=  abs(board[x][y] - board[xx][yy]) <= r:
            dfs(xx, yy)
            
    
answer = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    routes = []
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                land = []
                dfs(i, j)
                routes.append(land)
                
    if len(routes) == n * n:
        break
    
    for route in routes:
        if len(route) < 2:
            continue
        avg = sum([board[x][y] for x, y in route]) // len(route)
        for x, y in route:
            board[x][y] = avg
            
    answer += 1



print(answer)


        
