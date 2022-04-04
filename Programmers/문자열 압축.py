def solution(s):
    n = len(s)
    answer = n
    
    for i in range(1, n//2 + 1):
        a = [s[k: k+i] for k in range(0, n, i)]
        m = len(a)
        
        res = ''
        cnt = 1
        
        for j in range(1, m):
            if a[j-1] == a[j]:
                cnt += 1
            else:
                if cnt > 1:
                    res += str(cnt)
                res += a[j-1]
                cnt = 1
        
        if cnt > 1:
            res += str(cnt)
        res += a[m-1]
        
        # print(res)
        
        answer = min(answer, len(res))
        
    
    return answer
