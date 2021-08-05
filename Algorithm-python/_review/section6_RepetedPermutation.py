def dfs(L):
     global count
     if L==m:
          for i in range(m):
               print(a[i], end=" ")
          print()
          count+=1
          return
     else:
          for i in range(1,n+1):
               a[L]=i
               dfs(L+1)
               
          


if __name__=="__main__":
     n,m=map(int,input().split())
     a=[-1]*m
     count=0
     dfs(0)
     print(count)
