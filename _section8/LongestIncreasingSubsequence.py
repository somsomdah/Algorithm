
n=int(input())

arr=list(map(int,input().split()))
arr.insert(0,0)

D=[0]*(n+1) #1~n 번째 까지 가장 긴 증가수열의 길이


for i in range(1,n+1): # i번째 숫자가 마지막일 때
     res=0
     for j in range(i-1,0,-1): #  j번째 숫자가 i번째 수 앞에 오는 수일 때
          #print(j)
          if arr[j]<arr[i]:
               res=max(res,D[j])

     D[i]=res+1
               

print(max(D))
     
