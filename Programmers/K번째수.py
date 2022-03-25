def solution(array, commands):

    res = []
    
    for c in commands:
        i, j, k = c
        a = array[i-1:j]
        a.sort()
        res.append(a[k-1])

    return res
