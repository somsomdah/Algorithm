import sys
from collections import deque


n,m=map(int,sys.stdin.readline().split())
weights=list(map(int,sys.stdin.readline().split())) #  승객의 무게 리스트

weights.sort()
# weights=deque(weights)

count=0
while weights:
     if len(weights)==1:
          count+=1
          break;
     if weights[0]+weights[-1]>m:
          weights.pop()
          count+=1
     else:
          weights.pop()
          weights.pop(0) #weights.popleft()
          count+=1
          
print(count)




'''
# 두명까지만 탑승 가능하다는 점을 고려하지 않음

weights.sort(reverse=True)
weights.sort()

count=0
left=140
checklist=[0]*n

for i in range(n):
     if checklist[i]==0:
          
          for j in range(i,n):
               if left-weights[j]>=0 and checklist[j]==0:                    
                    left-=weights[j]
                    checklist[j]=1
          else:               
               count+=1
               left=140

print(count)
'''
