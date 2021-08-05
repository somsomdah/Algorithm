import sys
#sys.stdin=open("in5.txt","rt")

n,k=list(map(int,input().split()))

count=0

for i in range(1,n+1):
     if n%i==0:
          count+=1
     if count==k:
          print(i)
          break;
else: # 모든 루프가 끝난 경우
     print(-1)
