
def digit_sum(x):
     res=0
     for i in range(len(str(x))):
          res+=(x//(10**i))%10
     return res




n=int(input())
nums=list(map(int,input().split()))

max_sum=0
ans=0

for num in nums:
     if max_sum<digit_sum(num):
          max_sum=digit_sum(num)
          ans=num


print(ans)

