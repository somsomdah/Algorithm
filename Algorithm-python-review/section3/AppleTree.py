n=int(input())

s,e=n//2,n//2+1
ans=0

for _ in range(n//2+1):
     
     temp=list(map(int,input().split()))
     ans+=sum(temp[s:e])     

     s-=1
     e+=1


s+=1
e-=1

for _ in range(n//2+1,n):

     s+=1
     e-=1
     
     temp=list(map(int,input().split()))
     ans+=sum(temp[s:e])
     

print(ans)
