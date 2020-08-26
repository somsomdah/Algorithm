import sys

n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))

def binarySearch(left,right,nums,m):    
     mid=(left+right)//2

     if nums[mid]==m:
          print(mid+1)
          return
     elif nums[mid]>m:
          binarySearch(left,mid-1,nums,m)
     elif nums[mid]<m:
          binarySearch(mid+1,right,nums,m)

nums.sort()
binarySearch(0,n-1,nums,m)

'''
lt,rt,a=0,n-1,nums
while(lt<=rt):
     mid=(lt+rt)//2
     if a[mid]==m:
          print(mid+1)
          break
     elif a[mid]>m:
          rt=mid-1
     else:
          lt=mid+1
'''
