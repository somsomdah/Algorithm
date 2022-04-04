# 자정부터 몇 ms가 지났는지
def simpleTime(time):
    a = time.split(':')
    res = 0 
    res += int(a[0]) * 3600
    res += int(a[1]) * 60
    res += float(a[2])
    res *= (10 ** 3)
    return res # 0.01sec 포함하는거 안헷갈리게

def simpleSec(sec):
    a = sec[:-1] # s 문자열 지움
    res = float(a) 
    return res * (10 ** 3)
    

def solution(lines):
    
    n = len(lines)
    pp = [] # postprocessed
    for l in lines:
        k = l.split()
        t, s = simpleTime(k[1]), simpleSec(k[2])
        pp.append([t-s+1, t]) # 양끝 포함
        
    pp.sort(key = lambda x: [x[1], x[0]])
    
    res = 0
    ps = sum(pp,[]) # 시작, 끝 모든 점 (points)
    ps.sort()
    
    for p in ps:
        n1 = 0
        n2 = 0
        for s, e in pp:
            if s <= p <= e:
                n1 += 1
                n2 += 1
            elif p-999 <= e < p :
                n1 += 1
            elif p <= s <= p+999:
                n2 += 1
            
        print(res, n1, n2)
        res = max([res, n1, n2])


    return res
