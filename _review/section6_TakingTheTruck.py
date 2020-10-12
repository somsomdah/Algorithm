def dfs(L,sum_,tsum):
     global result

     if sum_+(total-tsum)<result:
          return

     if sum_>c:
          return
     if L==n:
          if result<sum_ and sum_<c:
               result=sum_
     else:
          dfs(L+1,sum_+a[L],tsum+a[L])
          dfs(L+1,sum_,tsum+a[L])



if __name__=="__main__":
     c,n=map(int,input().split())
     a=[int(input()) for _ in range(n)]
     total=sum(a)
     result=0

     dfs(0,0,0)
     print(result)

# tsum : 판단할 바둑이의 무게
# total-tsum : 앞으로 판단 할 바둑이의 총 무게
# (total-tsum)+sum_<result ->가지를 더 뻗어나갈 필요 없음
