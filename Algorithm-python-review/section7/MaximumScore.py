n,m=map(int,input().split())
q=[]
for _ in range(n):
     q.append(tuple(map(int,input().split())))

ans=0

def dfs(L,score,time):

     global ans

     if time>m:
          return


     if L==n:
          ans=max(ans,score)
          return

     else:
          dfs(L+1,score+q[L][0],time+q[L][1])
          dfs(L+1,score,time)


dfs(0,0,0)
print(ans)
