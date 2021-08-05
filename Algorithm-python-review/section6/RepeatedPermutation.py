n,m=map(int,input().split())

res=[0]*m
count=0


def dfs(L):
     global res,count
     if L==m:
          for num in res:
               print(num,end=' ')
          print()
          count+=1
          return

     else:
          for i in range(1,n+1):
               res[L]=i
               dfs(L+1)


dfs(0)
print(count)
