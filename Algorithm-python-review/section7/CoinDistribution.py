n=int(input())

coins = [int(input()) for _ in range(n)]

min_diff=sum(coins)


def dfs(L,a,b,c):
     global min_diff
     
     if L==n:          
          if a!=b and b!=c and a!=c:
               diff = max(a,b,c)-min(a,b,c)
               min_diff = min(min_diff,diff)
          
     else:
          
          dfs(L+1,a+coins[L],b,c)
          dfs(L+1,a,b+coins[L],c)
          dfs(L+1,a,b,c+coins[L])


dfs(0,0,0,0)

print(min_diff)
