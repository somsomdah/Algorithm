import sys

n=int(sys.stdin.readline())

wreslers=[]
for _ in range(n):
     h,w=map(int,sys.stdin.readline().split())
     wreslers.append([h,w])

wreslers=sorted(wreslers,reverse=True)

maxx=0
count=0
for _,w in wreslers:
     if w>maxx:
          count+=1
          maxx=w
          
print(count)
