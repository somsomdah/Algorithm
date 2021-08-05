import sys

n,m=map(int,input().split())

D=[[5000000000]*(n+1) for _ in range(n+1)]

for _ in range(m):
     s,e,c=map(int,input().split())
     D[s][e]=c

for i in range(0,n+1):
     D[i][i]=0

for k in range(1,n+1):
     for i in range(1,n+1):
           for j in range(1,n+1):
                D[i][j]=min(D[i][k]+D[k][j],D[i][j])


for i in range(1,n+1):
     for j in range(1,n+1):
          if D[i][j]==5000000000:
               print("M",end=' ')
          else:
               print(D[i][j],end=' ')

     print()

