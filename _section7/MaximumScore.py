
def dfs(L,s,t):
     global res

     if t>m:
          return;
     
     if L==n:
          if res<s:
               res=s
     else:
          dfs(L+1,s,t)
          dfs(L+1,s+ps[L],t+pt[L])



if __name__=="__main__":
     
     n,m=map(int,input().split())

     pt,ps=[],[]

     for _ in range(n):
          s,t=map(int,input().split())
          pt.append(t)
          ps.append(s)

     res=-1


     dfs(0,0,0)
     print(res)
