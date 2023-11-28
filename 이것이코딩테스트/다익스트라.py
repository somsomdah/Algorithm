import heapq

INF = int(1e9)


def dijkstra(n, m, start, info):

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for i in range(m):
        v1, v2, d = info[i]
        graph[v1] .append((v2, d))

    pq = [] # priority queue

    heapq.heappush((0,start))
    distance[start] = 0


    while queue:
        d1, v1 = heapq.heappop(pq)

        if distance[v1] < d1:
            continue

        for v in range(n):
            v2, d = graph[v]
            d2 = d1 + d

            if d2 < distance[v2]:
                distance[v2] = cost
                heapq.heappush(hq, (d2, v2))
