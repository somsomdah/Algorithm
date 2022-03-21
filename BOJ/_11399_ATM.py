n = int(input())

p = list(map(int,input().split()))

p.sort()

sum_ = 0


for i in range(n):
     sum_ += p[i] * (n-i)

print(sum_)
