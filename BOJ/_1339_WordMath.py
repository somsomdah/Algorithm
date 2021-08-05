
n=int(input())

answer={}
for _ in range(n):
     line=[c for c in input()]
     line.reverse()
     for i,c in enumerate(line):
          if c in answer.keys():
               answer[c]+=10**i
          else:
               answer[c]=10**i

temp=list(answer.values())
temp.sort(reverse=True)

res=0
for i,num in enumerate(temp):
     res+=(9-i)*num

print(res)
