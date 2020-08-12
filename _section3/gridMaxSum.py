'''
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.
'''
import sys

n=int(sys.stdin.readline())
a=[ list(map(int,sys.stdin.readline().split())) for _ in range(n)]


largest=-1
for i in range(n):
     sum1=sum2=0
     for j in range(n):
          sum1+=a[i][j]
          sum2+=a[j][i]
     if sum1>largest:
          largest=sum1
     if sum2>largest:
          largest=sum2



sum1=sum2=0
for i in range(n):
     sum1+=a[i][i]
     sum2+=a[i][n-1-i]

if sum1>largest:
     largest=sum1
if sum2>largest:
     largest=sum2


print(largest)


# Wrong Answer
'''
grid=[]
maxi=0

for _ in range(n):
     row=list(map(int,sys.stdin.readline().split()))
     grid.append(row)

     temp=sum(row)
     if maxi<temp:
          maxi=temp

for i in range(n):
     temp=sum([grid[i][j] for j in range(n)])
     if maxi<temp:
          maxi=temp


temp1=sum([grid[i][i] for i in range(n)])
temp2=sum([grid[n-1-i][i] for i in range(n)])


maxi=max([maxi,temp1,temp2])

print(maxi)
'''
