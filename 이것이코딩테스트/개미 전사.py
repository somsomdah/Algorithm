n = int(input())

food =list(map(int, input().split()))




D = [0] * n
D[0] = food[0]
D[1] = max(food[0], food[1])

for i in range(2, n):

    D[i] = max(D[i-1], D[i-2] + food[i])

print(D[n-1])
