

def dfs(L,sum_):

     if L==k:
          if sum_>0:
               res[sum_-1]=1

     else:
          dfs(L+1,sum_+a[L])
          dfs(L+1,sum_)
          dfs(L+1,sum_-a[L])

          #print(sum_,a[L])





if __name__=="__main__":

     k=int(input())
     a=list(map(int,input().split()))
     a.sort(reverse=True)
     s=sum(a)

     
     res=[0]*s
     

     dfs(0,0)

     #print(res)
     print(res.count(0))
