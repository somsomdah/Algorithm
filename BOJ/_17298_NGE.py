n = int(input())
nums = list(map(int, input().split()))
stack = [] # n의 인덱스

ans = [-1 for _ in range(n)]

for i in range(n): # 현재 수의 인덱스
    #스택이 비지 않았으면서, 이전 수보다 현재 수가 크면
    while stack and nums[stack[-1]] < nums[i]:
        
        # 이전 수의 오큰수는 현재 수
        ans[stack.pop()] = nums[i]

    # 스택이 비었거나 이전 수보다 현재 수가 작으면
    stack.append(i)
    
print(*ans)
