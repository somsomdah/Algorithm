n=int(input())

D=[[0]*10 for _ in range(n+1)]
# D[i][j] : 길이가 i이고 마지막 숫자가 j인 계단수의 갯수

D[1]=[1]*10
D[1][0]=0

for i in range(2,n+1):
     for j in range(10):
          if j==0:
               D[i][j]=D[i-1][j+1]
          elif j==9:
               D[i][j]=D[i-1][j-1]
          else:
               D[i][j]=D[i-1][j+1]+D[i-1][j-1]

for d in D:
     print(d)


print(sum(D[n])% 1000000000)

