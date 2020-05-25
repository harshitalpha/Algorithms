n = int(input())
arr = [int(s) for s in input().split()]
dp = [1]*n
for i in range(1,n):
    if dp[i] == 1:
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            if arr[i] > arr[i-2]:
                dp[i] = dp[i-2] + 1
            elif arr[i+1] > arr[i-1]:
                dp[i+1] = dp[i-1] + 1
            else:
                dp[i] = 1
print(max(dp))