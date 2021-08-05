import sys


n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

max_val=sys.maxsize

mat=[[max_val]*(n+1) for _ in range(n+1)]

#for i in range(1,n+1):
     #mat[i][i]=0

for _ in range(m):
     i,j,c=map(int,sys.stdin.readline().split())
     mat[i][j]=min(c,mat[i][j])


for i in range(1,n+1):
     for j in range(1,n+1):
          for k in range (1,n+1):
               if j==k:
                    mat[j][k]=0
               else:
                    mat[j][k]=min(mat[j][k],mat[j][i]+mat[i][k])



for i in range(1,n+1):
     for j in range(1,n+1):
          if mat[i][j]==max_val:
               mat[i][j]=0


for i in range(1,n+1):
     for j in range(1,n+1):
          print(mat[i][j], end=' ')
     print()
