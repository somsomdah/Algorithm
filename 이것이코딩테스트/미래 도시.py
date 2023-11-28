INF = int(1e9)


n, m = map(int, input().split())

graph = [INF for _ in range(n+1)] * (n+1)

for i in range(n+1):
    graph[i][i] = 0

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

x, k = map(int, input().split())

for l in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][l] + graph[l][j])


if graph[1][k] >= INF:
    print(-1)
elif  graph[k][x] >= INF:
    print(-1)
else:
    print(graph[i][k] + graph[k][x])

    
    
