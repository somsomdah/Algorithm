import sys
input = sys.stdin.readline
n = int(input())
m = n+1

answer = 0

for i in range(1, n):
    answer += m * i

print(answer)
