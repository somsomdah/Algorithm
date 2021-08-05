
n=int(input())
arr=[int(input()) for _ in range(n)]
arr.insert(0,0)

D=[0]*(n+1)



if n==1:
     print(arr[1])
elif n==2:
     print(arr[1]+arr[2])
else:
     D[1],D[2],D[3]=arr[1],arr[1]+arr[2],max(arr[1]+arr[3],arr[2]+arr[3])

     for i in range(3,n+1):
          D[i]=max(D[i-2]+arr[i],D[i-3]+arr[i-1]+arr[i])
          
     print(D[n])

