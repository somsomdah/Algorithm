n,m=map(int,input().split())

min_num=min(m,n)
max_num=max(m,n)

mid=(2+n+m)//2
start=min_num+1
end=2*mid-start

for i in range(start,end+1):
     print(i,end=' ')
