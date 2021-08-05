import sys

def dfs(L,sum_):

     if sum_>total-sum_:
          return;
     if L==n:
          if (sum_==total-sum_):
               print("YES")
               sys.exit(0)
     else:
          dfs(L+1,sum_)
          dfs(L+1,sum_+nums[L])

if __name__=='__main__':
     n=int(input())
     nums=list(map(int,input().split()))
     total=sum(nums)
     dfs(0,0)
     print("NO")
