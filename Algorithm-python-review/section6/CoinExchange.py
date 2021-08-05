import sys
n=int(input())

coins=list(map(int,input().split()))
coins.sort(reverse=True)

total=int(input())
ans=sys.maxsize

def dfs(L,sum):
     global ans
     if L>ans:
          return
     if sum>total:
          return
     if sum==total:
          ans=min(ans,L)
     else:
          for c in coins:
               dfs(L+1,sum+c)

dfs(0,0)
print(ans)
