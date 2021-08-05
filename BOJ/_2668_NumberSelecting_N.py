


# !!!!!!!!!!!!!!!!!!!!시간 초과!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# 완성하기
n=int(input())

a=[-1]

for _ in range(n):
     a.append(int(input()))
              
total=-1
visited=[0]*(n+1)
res=[0]*(n+1)
ans=[]

dfs(v):
     if v==n:
          if visited==res:
               if sum(visited)>total:
                    total=sum(visited)
                    ans=[i for i in range(1,n+1) if visited[i]==1]
     else:
          if visited[v]==0:
               visited[v]==1
               dfs(v)
               visited[v]==0
                    
     






                    
