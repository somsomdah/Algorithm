t = int(input())
k = int(input())

coins = [tuple(map(int,input().split())) for _ in range(k)]

coins.sort(reverse=True)


res = 0

def dfs(L,sum):
     
     global res
     
     if sum>t:
          return
     if L==k:
          if sum==t:
               res+=1
     else:
          for i in range(coins[L][1]+1):
               dfs(L+1,sum+coins[L][0]*i)

dfs(0,0)

print(res)
