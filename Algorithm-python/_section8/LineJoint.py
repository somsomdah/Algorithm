
n=int(input())

arr=list(map(int,input().split()))
arr.insert(0,0)

D=[0]*(n+1)

for i in range(1,n+1): # 수열의 마지막이 i 
     res=0
     for j in range(i-1,0,-1):
          if arr[j]<arr[i]:
               res=max(res,D[j])

     D[i]=res+1

print(max(D))
