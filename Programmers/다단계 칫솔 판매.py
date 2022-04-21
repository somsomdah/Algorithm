def solution(enroll, referral, seller, amount):
    
    
    n = len(enroll)
    
    profits = [0 for _ in range(n)]
    idcs = {'-': n}
    
    for i in range(n):
        idcs[enroll[i]] = i
        
    for s, a in zip(seller, amount):
        
        idx = idcs[s]
        prft = a * 100
        
        while idx != n:
            
            if prft == 0:
                break
            
            tmp = prft // 10
            profits[idx] += prft - tmp
            
            idx = idcs[referral[idx]]
            prft = tmp
    
    return profits
