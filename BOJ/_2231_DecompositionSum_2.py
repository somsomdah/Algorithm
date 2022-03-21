n = int(input())

k = len(str(n))


for i in range(max(n - k*9,0),n+1):
     j = i
     sum_ = i
     for _ in range(k):
          sum_ += i%10
          i = i // 10
     if sum_ == n:
          print(j)
          break
else:
     print(0)
          
