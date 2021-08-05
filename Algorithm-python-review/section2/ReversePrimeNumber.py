
n=int(input())
nums=list(map(int,input().split()))

def reverse(x):
     list_x=[int(i) for i in str(x)]
     res=0
     for i in range(len(list_x)):
          res+=list_x[i]*(10**i)
     return res

def is_prime(x):
     if x==1:
          return False
     for i in range(2,x//2+1):
          if x%i==0:
               return False
     else:
          return True

for num in nums:
     reverse_num=reverse(num)
     if is_prime(reverse_num):
          print(reverse_num)
          
