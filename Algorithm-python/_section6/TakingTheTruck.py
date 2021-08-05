
def DFS(L,sum_,tsum):
     global result
     if sum_+total-tsum<result:
          return
     if sum_>c:
          return
     if L==n:
          if sum_>result:
               result=sum_
     else:
          DFS(L+1,sum_+a[L],tsum+a[L])
          DFS(L+1,sum_,tsum+a[L])



if __name__=="__main__":
     c,n=map(int,input().split())
     a=[]
     for _ in range(n):
          a.append(int(input()))


     result=-1000000
     total=sum(a)
     DFS(0,0,0)
     print(result)

     
# 시간초과
'''
def DFS(v):
     if v==n+1:
          temp=0
          global max_
          for i in range(1,n+1):
               temp+=weights[i-1]*checklist[i]
          if temp<=c:
               max_=max(temp,max_)
          return
     else:
          checklist[v]=0
          DFS(v+1)
          checklist[v]=1
          DFS(v+1)



if __name__=="__main__":

     c,n=map(int,input().split())
     weights=[]
     for _ in range(n):
          weights.append(int(input()))

     checklist=[-1]*(n+1)
     max_=0

     DFS(1)

     print(max_)
'''
