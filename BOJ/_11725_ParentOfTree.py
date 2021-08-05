import sys

n=int(sys.stdin.readline())

adj_list=[[] for _ in range(n+1)]

for _ in range(n-1):
     v1,v2=map(int,sys.stdin.readline().split())
     adj_list[v1].append(v2)
     adj_list[v2].append(v1)


parent=[0]*(n+1)

Q=[1]

while Q:
     v=Q.pop(0)
     for child in adj_list[v]:

          parent[child]=v
          adj_list[child].remove(v)
     Q.extend(adj_list[v])

     #print(Q)

for i in range(2,n+1):
     print(parent[i])
          





'''
# 메모리 초과
import sys

n=int(sys.stdin.readline())

adj_mat=[[0]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
     i,j=map(int,sys.stdin.readline().split())
     adj_mat[i][j]=1
     adj_mat[j][i]=1

     

adj_list=[[] for _ in range(n+1)]


Q=[1]

while Q:
     v=Q.pop(0)

     for i in range(1,n+1):
          if adj_mat[v][i]==1:
               adj_list[v].append(i)
               adj_mat[v][i],adj_mat[i][v]=0,0
               Q.append(i)



parent=[0]*(n+1)

for i in range(1,n+1):
     childs=adj_list[i]
     for c in childs:
          parent[c]=i

for i in range(2,n+1):
     print(parent[i])
'''
