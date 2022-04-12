def solution(citations):
    n = len(citations)
    
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    
    for i in range(1, n+1): # 인용수가 가장 많은 논문부터 차례로
        if citations[i-1] >= i: # 인용수가 i번째로 많은 논문의 인용수가 i 이상이라면
            answer = i
        else:
            break
    
    return answer
