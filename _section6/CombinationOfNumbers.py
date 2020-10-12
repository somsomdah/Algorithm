def dfs(L,s,sum_):
     global count
     if L==k:
          if sum_%m==0:
               count+=1
     else:
          for i in range(s,n):
               res[L]=a[i]
               dfs(L+1,i+1,sum_+a[i])
               
          


if __name__=="__main__":
     n,k=map(int,input().split())
     a=list(map(int,input().split()))
     m=int(input())

     res=[0]*k
     count=0
     dfs(0,0,0)
     print(count)
     
