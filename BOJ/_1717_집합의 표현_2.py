n, m = map(int, input().split())

parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):

    if a == b:
        return
    roota, rootb = find(a), find(b)
    
    if roota== rootb:
        return
    if rank[a] == rank[b]:
        rank[a] += 1
        
    if rank[a] > rank[b]:
        rank[a] += rank[b]
        parent[rootb] = roota
    elif rank[b] > rank[a]:
        rank[b] += rank[a]
        parent[roota] = rootb


for _ in range(m):
    o, a, b = map(int, input().split())

    if o == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
