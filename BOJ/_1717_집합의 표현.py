import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def union(a, b):

    if a == b:
        return

    pa = find(a)
    pb = find(b)

    if pa == pb:
        return

    if pa > pb:
        a, b = b, a
        pa, pb = pb, pa  # pa < pb
      
    parent[pb] = pa
    parent[a], parent[b] = pa, pa
    
     
        
def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a,b)
    if o == 1:
        roota = find(a)
        rootb = find(b)
        if roota == rootb:
            print("YES")
        else:
            print("NO")
