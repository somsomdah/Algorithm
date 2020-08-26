import sys

k,n=map(int,sys.stdin.readline().split())




'''
# recursion depth exceded
cables=[]
for _ in range(k):
     cables.append(int(sys.stdin.readline()))

cables.sort()

def maxLength(nums,n,min_length,max_length):
     mid=(min_length+max_length)//2

     n1=sum([num//max_length for num in nums])
     n2=sum([num//mid for num in nums])
     n3=sum([num//min_length for num in nums])
     #print([num//max_length for num in nums])
     #print([num//mid for num in nums])
     #print([num//min_length for num in nums])
     #print(n,n1,n2,n3)
     if n==n2 or n==n1 or n==n3:
          print(mid)
          return
     elif n1<n and n<n2:
          maxLength(nums,n,mid,max_length)
     elif  n2<n and n<n3:
          maxLength(nums,n,min_length,mid)

maxLength(cables,n,1,cables[-1])
'''
