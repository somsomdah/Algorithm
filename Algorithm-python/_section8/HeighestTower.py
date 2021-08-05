

n=int(input())
D=[0]*n

arr=[]
for _ in range(n):
     a,h,w=map(int,input().split())
     arr.append([a,h,w])

arr.sort(reverse=True)


for i in range(n):
     temp=0
     for j in range(i-1,-1,-1):
          if arr[j][2]>arr[i][2]:
               temp=max(D[j],temp)
     
     D[i]=temp+arr[i][1]
     
#print(D)
print(max(D))

