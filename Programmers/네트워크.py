def solution(n, computers):
    
    visited = [0 for _ in range(n)]
    
    def dfs(v):
        visited[v] = 1
        
        for i in range(n):
            if computers[v][i] == 1 and visited[i] == 0:
                dfs(i)
    
    count = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            count += 1

    return count
