import sys
input = sys.stdin.readline

def solution(x, n, l):
    if n < 2:
        return "danger"

    l.sort()
    s, e = 0, n-1

    while s < e:
        m = l[s] + l[e]
        if m == x:
            return "yes {} {}".format(l[s], l[e])
        if m > x:
            e -= 1
        elif m < x:
            s += 1
            
    return "danger"

while True:
    try:
        x = int(input()) * (10 ** 7)
        n = int(input())
        l = [int(input()) for _ in range(n)]
        print(solution(x, n, l))
    except:
        break
