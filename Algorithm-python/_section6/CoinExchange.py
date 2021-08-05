import sys

def DFS(L,sum_):
     global answer
     if L>answer: #갱신이 되던 되지않던 답보다 크면
          return
     if sum_>result:
          return
     if sum_==result:
          if L<answer: # 더 적은 값으로 답 갱신
               answer=L
     else:
          for i in range(n):
               DFS(L+1,sum_+coins[i])
#               DFS(L+1,sum_)



if __name__=="__main__":
     n=int(input())
     coins=list(map(int,input().split()))
     result=int(input())

     coins.sort(reverse=True) # 큰 단위부터 세는 것이 빠름!!!!
     answer=1000000000
     
     DFS(0,0)
     print(answer)
