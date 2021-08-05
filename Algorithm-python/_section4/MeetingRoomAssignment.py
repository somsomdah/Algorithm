import sys

n=int(sys.stdin.readline())

mr=[]
for i in range(n):
     s,e=map(int,sys.stdin.readline().split())
     mr.append([s,e])

mr=sorted(mr, key=lambda x:(x[1],x[0])) # 끝나는시간 기준으로 정렬->끝나는 시간이 같으면 시작시간 기준으로 정렬

end=-1
count=0
for item in mr:
     if end<=item[0] : # 현재 회의의 start 시간이 이전 회의의 end 시간보다 늦으면
          end=item[1]
          count+=1
     
print(count)
