


def DFS(L,sum_):
     global count
     if L>=n:
          if sum_==s:
               count+=1
               return
     else:
          DFS(L+1,sum_+arr[L])
          DFS(L+1,sum_)



if __name__=="__main__":
     n,s=map(int,input().split())
     arr=list(map(int,input().split()))
     
     count=0

     DFS(0,0)

     if s:
          print(count)
     else:
          print(count-1)
     
