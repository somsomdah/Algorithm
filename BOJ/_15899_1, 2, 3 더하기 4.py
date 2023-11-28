import sys
input = sys.stdin.readline
t = int(input())

D = [[0, 0, 0, 0] for _ in range(10001)] # D[i][j] : i를 나타낼 수 있는 수 중에 j가 가장 큰 수 인 경우
D[1] [1]= 1
D[2][1] = 1
D[2][2] = 1
D[3][1] = 1
D[3][2] = 1
D[3][3] = 1

for i in range(4, 10001):
    D[i][1] = 1
    D[i][2] = D[i-2][2] + D[i-2][1]
    D[i][3] = D[i-3][3] + D[i-3][2] + D[i-3][1]

for _ in range(t):
    n = int(input())
    print(sum(D[n]))
