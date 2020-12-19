
n,c=map(int,input().split())


D=[0]*(c+1)

for i in range(n): # index i 번째 보석까지 적용
     w,v=map(int,input().split())
     # print(w,v)
     
     for j in range(w,c+1): #capacity  ~n까지
          D[j]=max(D[j-w]+v,D[j])


print(D[c])
          



