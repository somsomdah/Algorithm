def transfrom(num, k):
    
    if num == 10:
        return str(num)
    
    res = ""
    
    while num:
        tmp = num % k
        num //= k
        res = str(tmp) + res
    
    return res

def checkPrime(num):
    if num < 2:
         return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True

def solution(n, k):
    
    transferred = transfrom(n, k)
    
    answer = 0
    
    nums = [int(num) for num in transferred.split('0') if num]
    
    for num in nums:
        if checkPrime(num):
            answer += 1
    
    return answer
