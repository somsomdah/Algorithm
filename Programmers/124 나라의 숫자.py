def solution(n):
    
    m = n
    res = ''
    
    while m:
        r = m % 3
        if r == 0:
            res = '4' + res
            m = (m-1) // 3
        else:
            res = str(r) + res
            m = m // 3
        
    
    
    answer = res
    return answer
