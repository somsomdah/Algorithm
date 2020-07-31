import random
import sys
import math

N,K=map(int,sys.stdin.readline().split())
C=list(map(int,sys.stdin.readline().split()))

L=set() #중복을 제거하기 위함

for i in range(N):
     for j in range(i+1,N):
          for k in range(j+1,N):
               L.add(C[i]+C[j]+C[k]) # set 자료구조에 add
          

res=list(L)
res.sort(reverse=True)
               
print(res[K-1])
