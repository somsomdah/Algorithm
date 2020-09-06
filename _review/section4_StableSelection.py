
n,c=map(int,input().split())

point=[]
for _ in range(n):
     point.append(int(input()))
point.sort()

lt,rt=1,max(point) # 가장 가까운 두 말의 거리의 범위

def Count(dist) : # 가장 가까운 두 말의 거리가 dist일 때 배치할 수 있는 말의 수
     count=1
     loc=min(point)

     for i in range(1,n):
          if point[i]-loc>=dist:
               loc=point[i]
               count+=1
     return count

res=0
while lt<=rt:
     mid=(lt+rt)//2 #가장 가까운 두 말의 거리가 mid 일 때
     if c<=Count(mid):
          res=mid
          lt=mid+1
     else:
          rt=mid-1

print(res)


