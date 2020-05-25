'''
    Maximum Sum Increasing Subsequence
'''
def solve(arr):
    dp = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        m = 0
        for j in range(i):
            if arr[j] <= arr[i]:
                if dp[j] > m:
                    m = dp[j]
        
        dp[i] = m + arr[i]
    return max(dp),dp

arr = [1,101,2,3,100,4,5]
ans, dp = solve(arr)
print(dp)
print(ans)

