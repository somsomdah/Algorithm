import sys

num,m=map(int,sys.stdin.readline().split())
num=[int(n) for n in str(num)]

stack=[]
count=m

for n in num:
     while stack and count>0 and stack[-1]<n:
          stack.pop()
          count-=1
     stack.append(n)
if count!=0:
     stack=stack[:-count]

print(''.join(map(str,stack)))
