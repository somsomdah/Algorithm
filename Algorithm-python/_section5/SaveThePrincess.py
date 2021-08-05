import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())
queue=list(range(1,n+1))
queue=deque(queue)

count=0
while len(queue)>1:
     count+=1
     
     if count==k:
          #queue.pop(0)
          queue.popleft()
          count=0
     else:
          #queue.append(queue.pop(0))
          queue.append(queue.popleft())
          
print(queue[0])
