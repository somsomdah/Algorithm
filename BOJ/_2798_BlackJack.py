
n,m=map(int,input().split())
cards=list(map(int,input().split()))

res=-1

for i in range(n):
     for j in range(i):
          for k in range(j):
               temp=cards[i]+cards[j]+cards[k]
               if temp<=m:
                    res=max(res,temp)


print(res)
