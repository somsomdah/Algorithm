def solution(clothes):
    
    a = {}
    
    for c in clothes:
        if c[1] in a.keys():
            a[c[1]] += 1
        else:
            a[c[1]] = 1

    answer = 1
        
    for v in a.values():
        answer *= (v + 1) # 모든 경우의 수

        
    answer -= 1 # 옷을 입지 않은 경우
    
    return answer
