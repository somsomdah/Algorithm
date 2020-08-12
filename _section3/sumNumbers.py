'''
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합
A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''

import sys

n,m=map(int,sys.stdin.readline().split())
seq=list(map(int,sys.stdin.readline().split()))


lt,rt=0,1 # 인덱스를 가리키는 포인터  lt, rt
tot=seq[0] # lt부터 rt전까지의 sum
cnt=0

while True:
     if tot<m: 
          if rt<n:
               rt+=1 #rt 한칸 증가
               tot+=seq[rt-1]
          else:
               break;
     elif tot==m:
          cnt+=1
          lt+=1 # lt 한칸 증가
          tot-=seq[lt-1]
     else: #tot>m
          lt+=1
          tot-=seq[lt-1]

print(cnt)



# Time Limit Exceeded
'''
count=0
temp=m
for i in range(n):
     temp=m
     for j in range(i,n):
          temp=temp-seq[j]
          if temp==0:
               count+=1
               break;
     
print(count)
'''
