import sys
n=int(input())

adj_mat=[[0]*(n+1)]

for _ in range(n):
     temp=list(map(int,input().split()))
     temp.insert(0,0)
     
     adj_mat.append(temp)

linked=[]

res=0


for i in range(1,n+1):
     for j in range(1,n+1):
          if adj_mat[i][j]<0:
               if i not in linked:
                    linked.append(i)
               res-=adj_mat[i][j]

not_linked=[i for i in range(1,n+1) if i not in linked]

res=res//2
count=0
rails=[]

while not_linked:
     min_dist=sys.maxsize
     old_v=0
     new_v=0
     for v1 in linked:
          for v2 in not_linked:
               if adj_mat[v1][v2]<min_dist:
                    min_dist=adj_mat[v1][v2]
                    old_v=v1
                    new_v=v2

     not_linked.remove(new_v)
     linked.append(new_v)
     adj_mat[old_v][new_v]=sys.maxsize
     adj_mat[new_v][old_v]=sys.maxsize
     
     res+=min_dist
     count+=1
     rails.append((old_v,new_v))

c,m=res,count
print(c,m)
for r in rails:
     v1,v2=r
     print(v1,v2)
     
               

     

