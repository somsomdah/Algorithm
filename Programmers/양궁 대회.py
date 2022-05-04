def solution(n, info):
    
    if sum(info) == 0:
        return [-1]
    
    info.reverse() # 인덱스와 점수를 같게 하기 위함
    
    lionInfo = [0 for _ in range(11)] 
    lionScore = -1
    apeachScore = 100
    
    result = [0] * 11
    
    def dfs(L, leftCount):
        
        nonlocal lionScore, apeachScore, result
        
        if leftCount < 0:
            return
        
        if leftCount == 0 or L == 11:
            
            tmpLionScore = 0
            tmpApeachScore = 0
            lionInfo[0] = max(0, n - sum(lionInfo))
            
            for i in range(11):
                
                if lionInfo[i] == info[i] == 0:
                    continue
                
                if lionInfo[i] > info[i]:
                    tmpLionScore += i
                else:
                    tmpApeachScore += i
                    
            if tmpLionScore-tmpApeachScore > lionScore-apeachScore:
                lionScore = tmpLionScore
                apeachScore = tmpApeachScore
                result = lionInfo[:]
                
                
            elif tmpLionScore-tmpApeachScore == lionScore-apeachScore:
                if lionInfo >  result:
                    lionScore = tmpLionScore
                    apeachScore = tmpApeachScore
                    result = lionInfo[:]
            
            lionInfo[0] = 0
            return
                
        
        # L점자리 쏴서 이기는 경우
        lionInfo[L] = info[L] + 1
        dfs(L+1, leftCount - lionInfo[L])
        
        # L점짜리 안 쏘는 경우
        lionInfo[L] = 0
        dfs(L+1, leftCount)
    
    
    dfs(0, n)
    
    if lionScore <= apeachScore:
        return [-1]

    # print(result)
    result.reverse()
    return result
