import sys

n,c=map(int,sys.stdin.readline().split())

Line=[]
for _ in range(n):
     Line.append(int(sys.stdin.readline()))

Line.sort()

''' 가장 가까운 두 말의 최대 거리가 length 일 때 배치할 수 있는 말의 최대 수'''
def Count(length):
     cnt=1
     ep=Line[0]
     for i in range(1,n):
          if Line[i]-ep>=length:
               cnt+=1
               ep=Line[i]
     return cnt

lt=1
rt=Line[n-1]
while lt<=rt:
     mid=(lt+rt)//2
     if Count(mid)>=c:
          res=mid
          lt=mid+1 # 더 긴 최소거리가 있는지 확인
     else:
          rt=mid-1 # 가장 인접한 거리가 너무 길다
          
print(res)




