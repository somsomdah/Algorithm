def sort(item):
    return sum([v[0] for v in item[1]])

def solution(genres, plays):
    
    n = len(genres)
    a = {}
    
    for i in range(n):
        pass
        if genres[i] in a.keys():
            a[genres[i]].append([plays[i],i])
        else:
            a[genres[i]] = [[plays[i], i]]
    
    
    b = list(a.items())
    b.sort(key=sort, reverse=True)
    
    res = []
    
    for k,v in b:
        tmp = sorted(v, key = lambda x: [-x[0],x[1]])
        if len(tmp) > 2:
            tmp = tmp[:2]
        res = res + [i[1] for i in tmp]
        
    return res
