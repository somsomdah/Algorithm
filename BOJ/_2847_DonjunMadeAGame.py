import sys

n=int(sys.stdin.readline())

level=[]
for _ in range(n):
     level.append(int(sys.stdin.readline()))
level.reverse()

count=0
for i in range(0,n-1):
     while level[i]<=level[i+1]:
          count+=1
          level[i+1]-=1

print(count)
