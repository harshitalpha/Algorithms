'''
    Maximum size square sub matrix with all 1's
'''
def solve(mat):
    r = len(mat)
    c = len(mat[0])
    dp = [[0 for i in range(c)] for j in range(r)]
    
    is_one = False
    for i in range(r):
        dp[i][0] = mat[i][0]
        if(mat[i][0] == 1):
            is_one = True


    for i in range(c):
        dp[0][i] = mat[0][i]
        if(mat[0][i] == 1):
            is_one = True
    
    if is_one:
        max_ans = 1
    else:
        max_ans = 0
    
    for i in range(1,r):
        for j in range(1,c):
            if mat[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if(dp[i][j] > max_ans):
                    max_ans = dp[i][j]
    
    print(dp)
    
    return max_ans

if __name__ == "__main__":
    mat = [[0,1,1,0,1],
           [1,1,0,1,0],
           [0,1,1,1,0],
           [1,1,1,1,0],
           [1,1,1,1,1],
           [0,0,0,0,0]]
    
    ans= solve(mat)
    print(ans)

    
