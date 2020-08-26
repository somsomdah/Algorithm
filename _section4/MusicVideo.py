import sys

n,m=map(int,sys.stdin.readline().split())
records=list(map(int,sys.stdin.readline().split()))
lt,rt=1,sum(records) # 하나의 dvd에 담을 수 잇는 용량의 범위

def count(records,cap): # dvd 하나의 용량이 cap일 때 필요한 최소 DVD 갯수
     count=1 #?
     summ=0
     for r in records:
          if summ+r<=cap:
               summ+=r
          else :
               count+=1
               summ=r
     return count

'''
res=0
while lt<=rt:
     mid=(lt+rt)//2
     if mid>=max(records) and count(records,mid)<=m:
          res=mid
          rt=mid-1
     else:
          lt=mid+1
          
print(res)

'''
# wrong
def binarySearch(records,lt,rt):
     
     mid=(lt+rt)//2 # 중간 용량
     
     if lt>rt:
          print(mid+1)
          return
     
     #dvd 최대 용량이 mid 일 때 필요한 dvd 수가, m보다 작거나 같으면
     if count(records,mid)<=m and mid>=max(records):
          binarySearch(records,lt,mid-1) # disk 용량 범위는 작은쪽으로 좁혀진다

     else: # count(records,mid)>m
          binarySearch(records,mid+1,rt) # disk 용량 범위는 큰쪽으로 좁혀진다

binarySearch(records,1,sum(records))          
       
