import sys

n=int(sys.stdin.readline())

rgb=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#print(rgb)

D=[[0]*3 for _ in range(n)]
D[0]=rgb[0]

for i in range(1,n):
     D[i][0]=min(D[i-1][1],D[i-1][2])+rgb[i][0] #i번째 집을 빨강으로 칠했을 때 최소값
     D[i][1]=min(D[i-1][0],D[i-1][2])+rgb[i][1] #i번째 집을 초록으로 칠했을 때 최소값
     D[i][2]=min(D[i-1][1],D[i-1][0])+rgb[i][2] #i번쨰 집을 파랑으로 칠했을 때 최소값

print(min(D[n-1][0],D[n-1][1],D[n-1][2]))





