n=int(input())
k=int(input())

q=k//n
r=k%n

if r==0:
     print(k)
else:
     i,j=q+1,r
     print(i,j)
     print(i*j)
