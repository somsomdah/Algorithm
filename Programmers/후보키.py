def solution(relation):
    r, c = len(relation), len(relation[0])
    candkeys = []
    
    # 유일성 판별
    def checkunique(key):
        if len(key) == 0:
            return False
        
        data = []
        for i in range(r):
            tmp = []
            for k in key:
                tmp.append(relation[i][k])
            if tmp in data:
                return False
            data.append(tmp)
        return True
    
    # 최소성 판별
    def checkmin(key):
        if len(key) == 0:
            return False
        for candkey in candkeys:
            if set(key) >= set(candkey): # candkey가 key의 부분집합
                return False
        return True
    
    
    queue = [[i] for i in range(c)]
    
    while queue:
        tmp = queue.pop(0)
        last = tmp[-1]
        
        if checkunique(tmp) and checkmin(tmp):
            candkeys.append(tmp)
            continue
        
        for i in range(last+1, c):
            queue.append(tmp+[i])
        
    
    print(candkeys)
    
    return len(candkeys)
