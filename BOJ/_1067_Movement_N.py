
import sys

n=int(sys.stdin.readline())

a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

res=0

for _ in range(n):

     sum=0
     
     for i in range(n):
          sum+=a[i]*b[i]


     res=max(res,sum)
     
     b.insert(0,b.pop())


print(res)
     
