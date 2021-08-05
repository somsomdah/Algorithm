

nv,ne=map(int,input().split()) # 정점 갯수, 간선 갯수
edges=[tuple(map(int,input().split())) for _ in range(ne)]
parent=list(range(nv+1)) # 선택된 노드가 없으니까 부모 노드는 자기 자신

total=0

def get_parent(v):
     if parent[v] == v:
          return v
     else:
          return get_parent(parent[v])



def select_edge(edge):
     global total
     v1,v2,c=edge
     
     a=get_parent(v1)
     b=get_parent(v2)

     # 더 작은 쪽이 부모 노드
     if a>b:     
          parent[a]=b
     else:
          parent[b]=a
          
     total+=c
     

def is_connected(v1,v2):
     if get_parent(v1)==get_parent(v2):
          return True
     else:
          return False


edges.sort(key=lambda x:x[2]) # 가중치 기준 오름차순 정렬

for edge in edges: # 가중치가 작은 순
     v1,v2,c=edge
     if not is_connected(v1,v2): # MST에서 현재 두 노드가 연결되어 있지 않다면 (사이클 방지)
          select_edge(edge) # 해당 간선 선택


print(total)
          
          
