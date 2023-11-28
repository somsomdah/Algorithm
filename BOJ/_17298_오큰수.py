from collections import deque

n = int(input())
stack = list(map(int, input().split()))
queue = deque()

answer = deque([-1])
queue.append(stack.pop())
while stack:
    # print(stack, queue)
    if not queue:
        answer.appendleft(-1)
        queue.appendleft(stack.pop())
        continue
    
    if stack[-1] < queue[0]:
        answer.appendleft(queue[0])
        queue.appendleft(stack.pop())
    else:
        queue.popleft()
    
        
for a in answer:
    print(a, end=" ")
