'''
Given a string s, find the longest palindromic continous substring in s.
You may assume that the maximum length of s is 1000.
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1 for i in range(len(s))] for j in range(len(s))]

        def solve(s, i, j):
            # print(i, j)
            if i > j:
                return ""
            if i == j:
                return s[i]
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:
                x = solve(s, i + 1, j - 1)
                if len(x) == j - i - 1:
                    # print("Hello")
                    dp[i][j] = s[i:j + 1]
                else:
                    r = solve(s, i + 1, j)
                    l = solve(s, i, j - 1)
                    if len(r) >= len(l):
                        dp[i][j] = r
                        # print(dp[i][j])
                    else:
                        dp[i][j] = l
                        # print(dp[i][j])
                return dp[i][j]
            else:
                r = solve(s, i + 1, j)
                l = solve(s, i, j - 1)
                if len(r) >= len(l):
                    dp[i][j] = r
                    # print(dp[i][j])
                    return dp[i][j]
                else:
                    dp[i][j] = l
                    # print(dp[i][j])
                    return dp[i][j]

        return solve(s, 0, len(s) - 1)
