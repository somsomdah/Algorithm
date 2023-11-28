from collections import deque
n, k = map(int, input().split())
nums = deque(list(map(int, [int(num) for num in input()])))
stack = list()

while nums:
    if not stack:
        stack.append(nums.popleft())
        continue
        
    if stack[-1] >= nums[0] and k > 0:
        stack.append(nums.popleft())
    elif k > 0:
        stack.pop()
        k -= 1
    else:
       break

if nums:
    stack += list(nums)
if k > 0:
    stack = stack[:-k]

for num in stack:
    print(num, end="")

