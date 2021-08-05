import sys

arr=list(range(1,21)) # range(21) 로 하면 0부터 21까지 생기기 때문에 인덱스로 헷갈릴 필요 없음
                         # 이후에 arr.pop((0)
for i in range(10): # for _ in range(10): 대입하는 시간을 줄일 수 있음
     a,b=map(int,sys.stdin.readline().split())
     '''
     arr2=arr[a-1:b]
     arr2.reverse()
     arr[a-1:b]=arr2
     '''
     for i in range((b-a)//2+1):
          arr[a-1+i],arr[b-1-i]=arr[b-1-i],arr[a-1+i]

for n in arr:
     print(n,end=" ")
