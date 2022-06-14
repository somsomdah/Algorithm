def solution(info, edges):
    
    n = len(info)
    tree = [[] for _ in range(n)]
    parent = [-1 for _ in range(n)]
    
    for edge in edges:
        p, c = edge
        tree[p].append(c)
        parent[c] = p
        
    res = 0
        
    def dfs(v, visited, sheepCnt, wolfCnt):
        
        if sheepCnt <= wolfCnt:
            return
        
        nonlocal res
        if res < sheepCnt:
            res = sheepCnt
                
        # 방문한 노드들의 자식들중 방문하지 않은 것들
        for i in range(n):
            if visited[i] == 1:
                for v2 in tree[i]:
                    if visited[v2] == 0: 
                        
                        visited[v2] = 1
                        if info[v2] == 0: sheepCnt += 1
                        else: wolfCnt += 1
                            
                        dfs(v2, visited, sheepCnt, wolfCnt)
                        
                        visited[v2] = 0
                        if info[v2] == 0: sheepCnt -= 1
                        else: wolfCnt -= 1
                    
    visited = [0]*n
    visited[0] = 1
    dfs(0, visited, 1, 0)
                        
    answer = res
    return answer
