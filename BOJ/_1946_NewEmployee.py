import sys

t=int(sys.stdin.readline())

for _ in range (t):
     n=int(sys.stdin.readline())
     p=[]
     for _ in range(n):
          a,b=(map(int,sys.stdin.readline().split()))
          p.append((a,b))

     p.sort()

     temp=p[0][1]
     count=0
     for person in p:
          if person[1]<=temp:
               temp=person[1]
               count+=1
               
     print(count)
          
               
          
