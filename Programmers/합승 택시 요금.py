INF = 10 ** 6

def solution(n, s, a, b, fares):
    
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    
    for f in fares:
        src, dst, cst = f
        graph[src][dst] = cst
        graph[dst][src] = cst
    
    for k in range(1, n+1): # 경유지점을 꼭 여기에!!!!!
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    graph[i][j] = 0
                    continue
                tmp = graph[i][k]+graph[k][j]
                if tmp < graph[i][j]:
                    graph[i][j] = tmp
    
    
    answer = INF
    

    for i in range(1, n+1):
        tmp = graph[s][i] + graph[i][a]+ graph[i][b]
        if tmp < answer:
            answer = tmp
        
    
    return answer
