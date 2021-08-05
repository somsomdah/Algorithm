c,n=map(int,input().split())
baduks=[int(input()) for _ in range(n)]
total=sum(baduks)


res=0
def dfs(L,sum,tsum):
     global res
     if sum+(total-tsum)<res:
          return
     
     if sum>c:
          return
     if L==n:
          if max(res,sum)<=c:
               res=max(res,sum)
          return
     else:
          dfs(L+1,sum+baduks[L],tsum+baduks[L])
          dfs(L+1,sum,tsum+baduks[L])


dfs(0,0,0)
print(res)
     
