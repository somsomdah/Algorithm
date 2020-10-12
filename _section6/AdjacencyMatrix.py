

p,q=map(int,input().split())

g=[[0]*(p+1) for _ in range(p+1)]

for _ in range(q):
     a,b,c=map(int,input().split())
     g[a][b]=c


for i in range(1,p+1):
     for j in range(1,p+1):
          print(g[i][j],end=" ")
     print()
