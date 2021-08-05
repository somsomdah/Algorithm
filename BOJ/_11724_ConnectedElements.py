import sys
sys.setrecursionlimit(10000) # 런타임 에러 방지

n, m = map(int, sys.stdin.readline().split()) # 정점의 갯수, 간선의 갯수

s = [[0] * (n + 1) for i in range(n + 1)] #인접 행렬
visit = [0 for i in range(n + 1)] # 방문한 노드 체크리스트
cnt = 0 # 연결 요소 갯수


for i in range(m): # 인접 행렬
    a, b = map(int, sys.stdin.readline().split())
    s[a][b] = 1
    s[b][a] = 1


# 정점 i에 대한 깊이 우선 탐색
def dfs(i):
    visit[i] = 1 # 해당 정점을 방문
    for k in range(1, n + 1):  # 모든 정점에 대해서
        if s[i][k] == 1 and visit[k] == 0: #정점 i와 연결되어 있고, 방문하지 않은 정점이라면
            dfs(k) #정점 k에 대한 깊이우선 탐색
            
    
for i in range(1, n + 1): # 정점 1~n에 대하여
     
    if visit[i] == 0: # 정점 i가 방문되지 않은 노드라면
        dfs(i) # 정점 i 에 대한 깊이 우선 탐색 -> 그래프 순회
        cnt += 1 # 하나의 그래프가 모두 탐색되면 카운트
        
print(cnt)
