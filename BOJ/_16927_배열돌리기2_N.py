import sys
sys.setrecursionlimit(2000)

n, m, r = map(int,sys.stdin.readline().split())

# x, y : current point
# s : (s, s) is the top left  point of the rectangle, it can be also represented as a depth
# rt : number of rotations
def rotate(x, y, s, rt):

    print(s, rt, x, y)
    
    if rt == 0:
        return (x, y)
    # (ex, ey) is the bottom right corner of the rectangle
    ex = n - 1 - s
    ey = m - 1 - s

    # top
    if x == s and s < y <= ey :
        if rt >= y - s:
            return rotate (x, s, s, rt - (y-s))
        else:
            return rotate(x, y-1, s, rt-1)
    # left
    if y == s and s <= x < ex:
        if rt >= ex - x:
            return rotate(ex, y, s, rt-(ex-x))
        else:
            return rotate(x+1, y, s, rt-1)

    # bottom
    if x == ex and s <= y < ey:
        if rt  >= ey - y:
            return rotate(x, ey, s, rt-(ey-y))
        else:
            return rotate(x, y+1, s, rt - 1)

    # right
    if y == ey and s < x <= ex:
        if rt >= x - s:
            return rotate(s, y, s, rt-(x-s))
        else:
            return rotate(x - 1, y, s, rt-1)

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [[0 for _ in range(m)] for _ in range(n)]



depth= min(m,n)//2

for i in range(n):
    for j in range(m):
        d = min([n-1-i, i, m-1-j, j])
        k = (n - 2 * d) * 2 + (m - 2 * d) * 2 - 4
        # k = 2 * n + 2 * m - 8 * d - 4
        rt = r % k
        x1, y1 = rotate(i, j, d, rt)
        result[x1][y1] = board[i][j]


for rr in result:
    print(*rr)


    
