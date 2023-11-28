import heapq
INF = 10001



n, m, c = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())

    graph[x].append((y, z))



distance = [INF] * (n+1)
distance[c] = 0

Q = []
heapq. heappush(Q, (0, c))

while Q:

    d, v = heapq.heappop(Q)

    if distance[v] < d:
        continue

    # v2에서 각 노드까지 거
    for v2, dtmp in graph[v]:
        d2= d + dtmp # v에서 각 노드까지 거

        if  d2 < distance[v2]:
            distance[v2] = d2
            heapq.heappush(Q, (d2, v2))


count = 0
totalt = 0

for i in range(1, n + 1):
    if distance[i] < INF:
        count += 1
        if totalt < distance[i]:
            totalt = distance[i]
count -= 1 # 시작 노드 제

print(count, totalt)






