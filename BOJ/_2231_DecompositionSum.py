import sys

n=int(sys.stdin.readline())

for i in range(n+1):
     digit_sum=sum([int(k) for k in str(i)])

     if digit_sum+i==n:
          print(i)
          break
else :
     print(0)
