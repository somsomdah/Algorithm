n=int(input())

grid=[list(map(int,input().split())) for _ in range(n)]

max_sum=0

for i in range(n):
     temp=sum(grid[i])
     max_sum=max(temp,max_sum)

for i in range(n):
     temp=sum([grid[r][i] for r in range(n)])
     max_sum=max(temp,max_sum)


max_sum=max(sum([grid[i][i] for i in range(n)]),max_sum)

max_sum=max(sum([grid[i][n-1-i] for i in range(n)]),max_sum)


print(max_sum)
