
n,m=map(int,input().split())
q=[(0,0)]

D=[0]*(m+1)


for i in range(n):
     s,t=map(int,input().split())
     for j in range(m,t-1,-1):
          D[j]=max(D[j],D[j-t]+s)

print(D[m])
