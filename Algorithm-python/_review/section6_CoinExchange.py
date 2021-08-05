def dfs(L,sum_):
     global result

     if L>result:
          return
     if sum_>total:
          return
     if sum_==total:
          if L<result:
               result=L
     else:
          for i in range(n):
               dfs(L+1,sum_+coins[i])


if __name__=="__main__":
     n=int(input())
     coins=list(map(int,input().split()))
     coins.sort(reverse=True) ###중요###
     total=int(input())
     result=10000000000
     #max_=max(coins)
     dfs(0,0)
     print(result)
