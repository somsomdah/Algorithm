def solution(s):
    
    n = len(s)    
    stack = []

    for i in range(n):
        tmp = s[i]
        
        if not stack:
            stack.append(tmp)
        else:
            if stack[-1] == tmp:
                stack.pop()
            else:
                stack.append(tmp)
                
        # print(stack)
    
    if stack:
        return 0
    else:
        return 1
