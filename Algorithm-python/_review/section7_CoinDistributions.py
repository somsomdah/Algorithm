

def dfs(L):
     global res
     if L==n:
          temp=max(p)-min(p)
          if temp<res and len(set(p))==3:
               res=temp
     else:
          for i in range(3):
               p[i]+=c[L]
               dfs(L+1)
               p[i]-=c[L]







if __name__=="__main__":

     n=int(input())

     c=[int(input()) for _ in range(n)]

     res=sum(c)

     p=[0,0,0]

     dfs(0)

     print(res)
