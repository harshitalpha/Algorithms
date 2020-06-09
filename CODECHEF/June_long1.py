for _ in range(int(input())):
    n, k = [int(s) for s in input().split()]
    arr = [int(s) for s in input().split()]
    ans = 0
    for i in arr:
        if i > k:
            ans = ans + (i-k)
    print(ans)