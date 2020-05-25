'''
    Count Even Length Binary Sequence With sum of first and second half bits
'''


def solve(n,diff):

    dp  =[[0 for i in range(n)] for j in range(-n,n+1)]

    dp[n+1][0] = 2
    dp[n][0] = 1
    dp[n+2][0] = 1

    for i in range(1,n):
        dp[n+1][i] = 2*dp[n+1][i-1] + dp[n][i-1] + dp[n+2][i-1]
        dp[n][i] = 2*dp[n][i-1] + dp[n-1][i-1] + dp[n+1][i-1]
        dp[n+2][i] = 2*dp[n+2][i-1] + dp[n+1][i-1] + dp[n+3][i-1]
        
    return dp[n+1][n-1]

n = 3
print(solve(n,0))