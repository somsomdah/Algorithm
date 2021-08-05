import math,sys

def combination(n,r):
    return int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

n,m=map(int,input().split())

res=[0]*n

def dfs(L):
    if L==n:
        ans=0
        for i in range(n):
            ans+=res[i]*combination(n-1,i)
        if ans==m:
            for r in res:
                print(r,end=' ')
            sys.exit(0)
    else:
        for i in range(1,n+1):
            if i not in res[:L]:
                res[L]=i
                dfs(L+1)

dfs(0)


    
