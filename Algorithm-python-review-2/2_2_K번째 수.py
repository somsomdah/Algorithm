t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr2 = arr[s-1:e]
    arr2.sort()
    ans = arr2[k-1]
    print("#{} {}".format(str(i+1), str(ans)))
