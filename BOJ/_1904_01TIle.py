import sys

n=int(sys.stdin.readline())

D=[0]*(n+1)

D[0]=1
D[1]=1

for i in range(2,n+1):
     D[i]=(D[i-1]+D[i-2])%15746

print(D[n])
