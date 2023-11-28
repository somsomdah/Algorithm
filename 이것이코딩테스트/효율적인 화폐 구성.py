n, m = map(int, input().split())
unit = [int(input()) for _ in range(n)]

unit.sort(reverse = True)


D = [0] *( m +1)
D[0] = 0


for u in unit:
    if u <= m:
        D[u] = 1

for i in range(1, m+1):
    
    for u in unit:
        if i - u> 0 and D[i-u] > 0 :
            if D[i] == 0:
                D[i] = D[i-u] + 1
            else:
                D[i] = min(D[i], D[i - u] + 1)

if D[m] == 0:
    print(-1)
else:
    print(D[m])

