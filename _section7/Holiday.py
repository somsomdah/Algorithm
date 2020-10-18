
def dfs(L,tot):

     #print(L,tot)
     global res
     
     if L>=n+1:
          if res<tot:
               res=tot
     else:
          if L+T[L]<=n+1:
               dfs(L+T[L],tot+P[L])
          dfs(L+1,tot)
          



if __name__=="__main__":

     n=int(input())

     T,P=[0],[0]

     for _ in range(n):
          t,p=map(int,input().split())
          T.append(t)
          P.append(p)
     

     res=0

     dfs(1,0)

     print(res)
