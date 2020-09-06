k,n=map(int,input().split())

length=list()
for _ in range(k):
     length.append(int(input()))

#length.sort()

def count(length_):
     cnt=0
     for l in length:
          cnt+=l//length_
     return cnt

lt,rt=1,max(length)

res=-1
while lt<=rt:
     mid=(lt+rt)//2
     if count(mid)>=n:
          res=mid
          lt=mid+1
     if count(mid)<n: # 길이가 mid 일때 랜선의 갯수
          rt=mid-1

print(res)
          

