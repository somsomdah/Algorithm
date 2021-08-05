import sys

n,m,v=map(int,input().split())

adj_mat=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
     v1,v2=map(int,input().split())
     adj_mat[v1][v2]=1
     adj_mat[v2][v1]=1
     

check1=[0]*(n+1)
check2=[0]*(n+1)

def dfs(v):
     check1[v]=1
     print(v,end=' ')
     for i in range(1,n+1):
          if check1[i]==0 and adj_mat[v][i]==1:
               dfs(i)


def bfs(v):
     queue=[v]
     check2[v]=1
     while queue:
          v=queue.pop(0)
          print(v, end=' ')
          for i in range(1,n+1):
               if check2[i]==0 and adj_mat[v][i]==1:
                    queue.append(i)
                    check2[i]=1





dfs(v)
print()
bfs(v)
