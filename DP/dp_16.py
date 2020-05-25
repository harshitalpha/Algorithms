'''
    Longest Common Substring
'''
def solve(str1,str2):
    m = len(str1)+1
    n = len(str2)+1
    dp = [[0 for j in range (m)] for i in range(n)]

    dp[0][0] = 0
    for i in range(1,n):
        dp[i][0] = 0

    for i in range(1,m):
        dp[0][i] = 0

    # all_cs = []
    # cs = []
    # reach_end = 0
    for i in range(1,n):
        for j in range(1,m):
            if str1[j-1] == str2[i-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                # if str1[j-1] not in cs:
                #     cs.append(str1[j-1])
                #     if j == m:
                #         reach_end = 1
                    
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        #print(reach_end)
    #     if reach_end == 1:
    #         all_cs.append(cs)
    #         cs = []

    # print(all_cs)
    print(dp)
    print(dp[n-1][m-1])



str1 = 'abcdxyz'
str2 = 'xyzabcd'
solve(str1,str2)
