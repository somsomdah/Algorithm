INF = 10 ** 5

    
def solution(n, vertices):
    
    adj = [[] for _ in range(n+1)]
    
    for v in vertices:
        v1, v2 = v
        adj[v1].append(v2)
        adj[v2].append(v1)
        
        
    neighbors = []
        
    dist = [0 for _ in range(n+1)]
    queue = [1]
    visited = [0 for _ in range(n+1)] # 이렇게 해야 시간초과 안 뜸!!
    visited[1] = 1
    
    while queue:
        current = queue.pop(0)
        for i in adj[current]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                dist[i] = dist[current] + 1
                
    maxdist = max(dist)
    count = dist.count(maxdist)
    
    return count
