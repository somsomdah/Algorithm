
n,m=map(int,input().split())

res=[0]*m
count=0

def dfs(L,s):
     global count
     if L==m:
          count+=1
          for r in res:
               print(r,end=' ')
          print()
     else:
          for i in range(s,n+1):
               res[L]=i
               dfs(L+1,i+1)

dfs(0,1)
print(count)
          
