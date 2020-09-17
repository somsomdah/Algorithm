import sys

def DFS(L,sum_) : # L ;  인덱스 번호(포인터), Level / sum_ : 부분집합 값을 누적
     if sum_>total//2:
          return
     if L==n:
          if sum_==(total-sum_): 
               print("YES")
               sys.exit(0)
     else:
          DFS(L+1,sum_+a[L])
          DFS(L+1,sum_)




if __name__=="__main__":
     n=int(input())
     a=list(map(int,input().split()))
     total=sum(a)

     DFS(0,0)
     print("NO")
