def solution(N, number):
    
    if number == N:
        return 1
    
    D = [[] for _ in range(9)] # D[i]: i개의 N으로 만들 수 있는 수의 리스트, 0 제외
    D[1] = [N]
    D[2] = [1, 2*N, N**2, 0, int(str(N)*2)]
    
    if number in D[2]:
        return 2
    
    for i in range(3, 9):
        
        rep = int(str(N)*i)
        if rep == number:
            return i
        D[i].append(rep)
        
        for j in range(1,i//2+1):
            
            for n1 in D[j]:
                for n2 in D[i-j]:
                    
                    sum = n1+n2
                    if sum in D[i]:
                        pass
                    elif sum == number:
                        return i
                    else:
                        D[i].append(sum)
                    
                    if n1 != n2:
                        sub = abs(n1-n2)
                        if sub in D[i]:
                            pass
                        elif sub == number:
                            return i
                        else:
                            D[i].append(sub)
                            
                    mul = n1*n2
                    if mul in D[i]:
                        pass
                    elif mul == number:
                        return i
                    else:
                        D[i].append(mul)
                    
                    if n1 == 0 or n2 == 0:
                        continue
                    div = n1//n2 if n1>n2 else n2//n1 
                    if div in D[i]:
                        pass
                    elif div == number:
                        return i
                    else:
                        D[i].append(div)
                        
    return -1
