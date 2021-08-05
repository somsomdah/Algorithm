n,m=map(int,input().split())

adj_list=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
     s,d=map(int,input().split())
     adj_list[s][d]=1


count=0
check=[0]*(n+1)
# res=[0]*n

def dfs(L,s):
     global count, res,check
     
     if L==n:
          return

     # res[L]=s
     
     if s==n:
          # print(res,L)
          count+=1
          return

     check[s]=1
     for i in range(1,n+1):
          if adj_list[s][i]==1 and check[i]==0:               
               dfs(L+1,i)
     check[s]=0


dfs(0,1)

print(count)
               
