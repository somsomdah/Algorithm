n=int(input())

A=[0]*n
B=list(map(int,input().split()))

count=0

while sum(B)!=0:
     
     if all(b%2==0 for b in B):
          B=[b//2 for b in B]
          count+=1
          continue
     
     for i in range(n):
          if B[i]%2!=0:
               B[i]-=1
               count+=1


print(count)
