# 해결 못함

n=int(input())
seq=list(map(int,input().split()))

res=[0]*n


for i in range(0,n):
     count=0
     for j in range(0,n):
          if res[j]==0:
               count+=1
          if count==seq[i]:
               res[j]=i+1

print(res)
