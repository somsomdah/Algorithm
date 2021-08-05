'''
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
'''

import sys
'''
def digit_sum(x):
     sum=0
     while x>0:
          sum+=x%10
          x=x//10
     return sum
'''
def digit_sum:
     sum=0
     for i in str(x):
          sum+=int(i)
     return sum
     

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

temp=[digit_sum(x) for x in a]
max=max(temp)
tempidx=temp.index(max)
print(a[tempidx])

'''
def digit_sum(number):
     count=0
     for i in range(1,8):
          temp=(number%(10**i))//(10**(i-1))
          count+=temp
          if temp==0:
               return count

N=int(sys.stdin.readline())
inp=list(map(int,sys.stdin.readline().split()))
temp=[digit_sum(num) for num in inp]
res=max(temp)
temp2=temp.index(res)
res2=inp[temp2]

print(res2)
'''

