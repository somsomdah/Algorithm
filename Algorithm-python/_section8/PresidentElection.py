import sys
n=int(input())

arr=[]
while(1):
     a,b=map(int,input().split())
     if a==-1 and b==-1:
          break
     arr.append((a,b))

m=len(arr)
adj_mat=[[sys.maxsize]*(n+1) for _ in range(n+1)]

for i in range(m):
     a,b=arr[i]
     adj_mat[a][b]=1
     adj_mat[b][a]=1


for k in range(1,n+1):
     for i in range(1,n+1):
          for j in range(1,n+1):
               if i==j:
                    adj_mat[i][i]=0
               else:
                    adj_mat[i][j]=min(adj_mat[i][j],adj_mat[i][k]+adj_mat[k][j])


res=[max(row[1:]) for row in adj_mat]

res_min=min(res)

ans=[]
for i in range(1,n+1):
     if res[i]==res_min:
          ans.append(i)


print(res_min,end=' ')
print(len(ans))

for a in ans:
     print(a,end=' ')
