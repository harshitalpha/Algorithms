t = int(input())
while t:
    t = t - 1
    n = int(input())
    a = [int(s) for s in input().split()]
    dp = [0 for i in range(n)]
    if a[0] >= 0:
        b = True
    else:
        b = False

    dp[0] = a[0]
    cur_sum = 0
    for i in range(n):
        if a[i] >= 0 and b:
            x = max(cur_sum,cur_sum+a[i])
            dp[i] = x
        elif a[i] < 0 and (not b):
            x = max(cur_sum,a[i])
            dp[i] = x
        else:
            dp[i] = dp[i-1] + a[i]
            cur_sum = dp[i]
            b = not b
    print(dp)