
n,m=map(int,input().split())
res=[0]*m
count=0

def dfs(L):
     global count,res
     
     if L==m:
          count+=1
          for num in res:
               print(num,end=" ")
          print()
          
     else:

          for i in range(1,n+1):
               if i not in res[:L]:
                    res[L]=i
                    dfs(L+1)



dfs(0)
print(count)
               
     
