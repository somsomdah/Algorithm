import sys
  
n,m=map(int,sys.stdin.readline().split())
queue=list(map(int,sys.stdin.readline().split()))

index=m
count=0
while True:
     #print(queue,index,count)
     if queue[0]>=max(queue):
          queue.pop(0)
          count+=1
          if index==0:
               break;
          else:
               index-=1
     else:
          queue.append(queue.pop(0))
          if index==0:
               index=len(queue)-1
          else:
               index-=1

print(count)
