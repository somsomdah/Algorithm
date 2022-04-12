import math
    

def solution(w,h):

    cnt = 0
    
    f = [0 for _ in range(w+1)]
    
    if h < w:
        w, h = h, w # 작은 것을 w로
    
    for x in range(1, w+1):
        f[x] = h * x / w
        cnt += math.ceil(f[x]) - math.floor(f[x-1])
        
        if f[x] % 1 == 0: # 1보다 큰 최대공약수 있음
            cnt = cnt * (w//x)
            break
        
    answer = w * h - cnt
    return answer
