'''
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저
있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사
과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서
남겨놓는다.
'''

import sys
n=int(sys.stdin.readline())
a=[ list(map(int,sys.stdin.readline().split())) for _ in range(n)]

res=0

s=e=n//2 # 포인터

for i in range(n): # 행
     for j in range(s,e+1):
          res+=a[i][j]
     if i<n//2:
          s-=1
          e+=1
     else:
          s+=1
          e-=1

print(res)





# Wrong Answer
'''
grid=[]
apple_sum=0

for i in range(n):
     row=list(map(int,sys.stdin.readline().split()))
     grid.append(row)

apple_sum=sum(grid[int(n/2)])
print(grid[int(n/2)])

for i in range(1,int(n/2)+1):
     apple_sum+=sum(grid[int(n/2)+i][i:-i])+sum(grid[int(n/2)-i][i:-i])
     print(grid[int(n/2)+i][i:-i],grid[int(n/2)-i][i:-i])

print(apple_sum)
'''    
