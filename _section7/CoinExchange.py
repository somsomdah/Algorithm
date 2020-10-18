
def dfs(L,s):

     global count

     if s>t:
          return
     
     if L>=k:
          if s==t:
               count+=1
     else:
          for i in range(N[L]+1):
               dfs(L+1,s+P[L]*i)




if __name__=="__main__":
     t=int(input())
     k=int(input())

     P,N=[],[]
     
     for _ in range(k):
          p,n=map(int,input().split())
          P.append(p)
          N.append(n)


     count=0
     dfs(0,0)
     print(count)
