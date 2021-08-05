import sys

n=int(sys.stdin.readline())

# 3kg 봉지의 갯수 a, 5kg 봉지의 갯수 b
# 3*a+5*b=n

for a in range (0,n//3+1):
     temp=n-3*a
     if temp%5==0:
          b=temp//5
          print(a+b)
          break
else:
     print(-1)
