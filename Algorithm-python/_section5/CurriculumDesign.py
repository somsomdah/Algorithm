from collections import deque

need=input()
n=int(input())

for i in range(n):
     plan=input()
     dq=deque(need)
     for x in plan:
          if x in dq:
              if  x!=dq.popleft():
                   print('#%d NO'%(i+1))
                   break
     else:
          if len(dq)==0:
               print("#%d YES" %(i+1))
          else:
               print("#%d NO"%(i+1))






# 성공한 코드
'''
import sys

essential=[e for e in sys.stdin.readline() if e!='\n']
n=int(sys.stdin.readline())

for i in range(n):
     classes=[c for c in sys.stdin.readline() if c!='\n']
     queue=[]
     for c in classes :
          if c in essential and c not in queue:
               queue.append(c)

     if queue==essential:
          print("#"+str(i+1)+" YES")
     else:
          print("#"+str(i+1)+" NO")
'''
