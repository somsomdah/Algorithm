
n=int(input())
c=list(map(int,input().split()))
m=int(input())

D=[m]*(m+1)
D[0]=0


for i in range(n):
     v=c[i]
     for j in range(v,m+1):
          D[j]=min(D[j],D[j-v]+1)


print(D[m])
