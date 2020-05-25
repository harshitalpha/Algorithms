import sys 
sys.setrecursionlimit(10**9)

'''
    EDIT DISTANCE
'''


def solve(str1, str2):
    n = len(str1)+1
    m = len(str2)+1

    dp = [[0 for j in range(m)] for i in range(n)]

    for i in range(1,m):
        dp[0][i] = 1

    for i in range(1,n):
        dp[i][0] = 1    

    for i in range(1,n):
        for j in range(1,m):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+1)
    
    return dp[n-1][m-1]

x = "sunday"
y = "saturday"
ans = solve(x,y)
print(ans)