for _ in range(int(input())):
    a, b = [int(s) for s in input().split()]
    m = min(a,b)
    ma = max(a,b)
    if ma > m*2:
        ans = m
    else:
        ans = int((m+ma)/3)
    print(ans)