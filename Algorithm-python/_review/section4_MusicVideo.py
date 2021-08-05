
n,m=map(int,input().split())
length=list(map(int,input().split()))

#length.sort()

lt,rt=0,sum(length)

#디스크 용량이 capacity일 떄 필요한 최소 디스크 수
def Count(capacity):
     count=1 #why????
     temp=capacity
     
     for l in length:
          if temp-l>=0:
               temp-=l
          else:
               temp=capacity-l
               count+=1    
     return count


while lt<=rt:
     mid=(lt+rt)//2
     res=0
     if mid>=max(length) and Count(mid)<=m :
          res=mid
          rt=mid-1
     if Count(mid)>m:
          lt=mid+1

print(res)
