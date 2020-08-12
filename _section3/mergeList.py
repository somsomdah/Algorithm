'''
두 리스트 합치기
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.
'''

import sys

n=int(sys.stdin.readline())
in1=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
in2=list(map(int,sys.stdin.readline().split()))


p1=p2=0
out=[]

while p1<n and p2<m:
     if in1[p1]<in2[p2]:
          out.append(in1[p1])
          p1+=1
     else:
          out.append(in2[p2])
          p2+=1

if p1<n:
     out=out+in1[p1:]
if p2<m:
     out=out+in2[p2:]

for o in out:
     print(o,end=' ')

'''
stack=[]

while len(in1)>0 and len(in2)>0:
     
     if in1[0]<in2[0]:
          stack.append(in1[0])
          in1.pop(0)
     else:
          stack.append(in2[0])
          in2.pop(0)

if len(in1)>len(in2):
     stack.extend(in1)
else:
     stack.extend(in2)

for s in stack:
     print(s,end=" ")
'''
