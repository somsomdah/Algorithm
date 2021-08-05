n=int(input())

a=[tuple(map(int,input().split())) for _ in range(n)]

ans=0

def dfs(L,days,pay):
     global ans
     
     if days>n:
          return
     if L>n:
          return
     
     if L==n:
          ans=max(pay,ans)
     else:
          dfs(L+1,days,pay)
          dfs(L+a[L][0],days+a[L][0],pay+a[L][1])




dfs(0,0,0)
print(ans)
          
