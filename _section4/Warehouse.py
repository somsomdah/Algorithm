import sys

l=int(sys.stdin.readline())
boxes=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())

boxes.sort()

for _ in range(m):
     boxes[0]+=1
     boxes[l-1]-=1
     boxes.sort()

#print(boxes)
print(boxes[l-1]-boxes[0])
