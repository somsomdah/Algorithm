
n=int(input())
schedules=[]

for _ in range(n):
     schedules.append(tuple(map(int,input().split())))

schedules.sort(key=lambda x:x[1])

count=0
end=0

for s in schedules:
     if s[0]>=end:
          count+=1
          end=s[1]
print(count)
