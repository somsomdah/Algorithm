import sys

T=int(sys.stdin.readline())

for i in range(T):
     N,s,e,k=map(int,sys.stdin.readline().split())
     C=list(map(int,sys.stdin.readline().split()))
     temp=C[s-1:e] # index!=@th
     temp.sort()
     C[s-1:e]=temp
     print("#"+str(i+1)+" "+str(C[k-1]))
     
