
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

lt,rt=-0,n-1

while lt<=rt:
     mid=(lt+rt)//2
     if m==a[mid]:
          print(mid+1)
          break
     if m<a[mid]:
          rt=mid-1
     if m>a[mid]:
          lt=mid+1
          
