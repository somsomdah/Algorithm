
n=int(input())
a=list(map(int,input().split()))
s=sum(a)
res = [0]*s

def dfs(L,total):
     if L==n:
          if total>0:
               res[total-1]=1
          
     else:
          dfs(L+1,total+a[L])
          dfs(L+1,total)
          dfs(L+1, total-a[L])

dfs(0,0)
print(res.count(0))
     
