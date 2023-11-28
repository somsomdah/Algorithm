import sys
input = sys.stdin.readline
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key = lambda x:(x[1],x[0]))
count = 0
s, e = 0, 0

for i in range(n):
    ss, ee = schedule[i]

    if e <=ss:
        count += 1
        s, e = ss, ee

print(count)
