import sys

n = int(input())
scores = [0]+ [int(input()) for _ in range(n)]


D = [0]*(n+1) # D[i] => i번째 계단을 밟았을 때의 최대 점수

if n < 2:
     print(scores[1])
     sys.exit(0)
     
elif n < 3:
     print(scores[1] + scores[2])
     sys.exit(0)
     
D[1] = scores[1]
D[2] = scores[1] + scores[2]
D[3] = max(scores[1], scores[2]) + scores[3]

for i in range(4, n+1):
     D[i] = max(D[i-3] + scores[i-1], D[i-2]) + scores[i]

print(D[n])

