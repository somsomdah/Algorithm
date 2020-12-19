n,m=map(int,input().split())

adj_mat=[[0]*(n+1) for _ in range(n+1)]
in_deg=[0]*(n+1)

for _ in range(m):
     a,b=map(int,input().split())
     adj_mat[a][b]=1
     in_deg[b]+=1


Q=[i for i in range(1,n+1) if in_deg[i]==0]
res=[]

while(Q):
     num=Q.pop(0)
     res.append(num)

     for i in range(1,n+1):
          
          if adj_mat[num][i]==1:
               in_deg[i]-=1

               if in_deg[i]==0:
                    Q.append(i)




print(res)
