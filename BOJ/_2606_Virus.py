

p=int(input())
q=int(input())

adj_mat=[[0]*(p+1) for _ in range(p+1)]
visit=[0]*(p+1)


for _ in range(q):
     v1,v2=map(int,input().split())
     adj_mat[v1][v2]=1
     adj_mat[v2][v1]=1


def dfs(v):

     for i in range(1,p+1):
          if adj_mat[v][i]==1 and visit[i]==0:
               visit[i]=1
               dfs(i)


visit[1]=1
dfs(1)

#print(visit)
print(sum(visit)-1)
