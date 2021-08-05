import sys

n=int(input())
nums=list(map(int,input().split()))

total=sum(nums)

def dfs(L,sum_):
     if sum_>total//2:
          return
     if L==n:
          if total-sum_==sum_:
               print("YES")
               sys.exit(0)
     else:
          dfs(L+1,sum_+nums[L])
          dfs(L+1,sum_)
          


dfs(0,0)
print('N0')

