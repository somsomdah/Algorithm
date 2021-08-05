import sys

n=int(input())

a=list(map(int,input().split()))

average=round(sum(a)/n)

std_num=list(range(1,n+1))


std_num.sort(key=lambda x : (abs(a[x-1]-average),max(a)-a[x-1],x))



print(average,std_num[0])
