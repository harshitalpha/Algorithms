'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
'''

class Solution:
    def solve(self, i, s):
        if s == "":
            return 1
        if s[0] == "0":
            return 0
        elif self.dp[i] != -1:
            return self.dp[i]
        else:
            if int(s[:2]) <= 26 and int(s[:2]) >= 10:
                self.dp[i] = self.solve(i + 1, s[1:]) + self.solve(i + 2, s[2:])
                return self.dp[i]
            else:
                self.dp[i] = self.solve(i + 1, s[1:])
                return self.dp[i]

    def numDecodings(self, s: str) -> int:
        self.dp = [-1] * len(s)
        # print(self.dp)
        return self.solve(0, s)


