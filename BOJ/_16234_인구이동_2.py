from collections import deque

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    result = []
    queue = deque([[x,y]])
    visited[x][y] = 1
    
    while queue:

        x, y = queue.popleft()
        result.append((x, y))
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0:
                if l <= abs(board[x][y] - board[xx][yy]) <= r:
                    visited[xx][yy] = 1
                    queue.append((xx, yy))
        
    avg = sum([board[x][y] for x, y in result]) // len(result)
    for x, y in result:
        board[x][y] = avg

answer = 0
while True:
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += 1
                bfs(i,j)

    if cnt == n * n:
        break

    answer += 1

print(answer)


