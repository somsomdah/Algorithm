n = int(input())


D = [0] * (n+1)

D[1] = 0

if n >= 2:
    D[2] = 1
if n >= 3:
    D[3] = 1


for i in range(4, n+1):

    D[i] = D[i-1]

    if i % 2 == 0:
        D[i] =min (D[i], D[i//2])
    if i % 3 == 0:
        D[i] = min(D[i], D[i//3])
        
    D[i] += 1

print(D[n])
