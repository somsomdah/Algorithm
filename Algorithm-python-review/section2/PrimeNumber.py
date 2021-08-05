
n=int(input())
ch=[0]*(n+1)

for i in range(2,n+1):

     k=2
     while i*k<=n:
          ch[i*k]=1
          k+=1

cnt=0
for i in range(2,n+1):
     if ch[i]==0:
          cnt+=1


print(cnt)

