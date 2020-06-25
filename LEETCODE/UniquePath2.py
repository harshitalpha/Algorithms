'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp  = [[0 for i in range(cols)] for j in range(rows)]
        if not obstacleGrid[0][0]:
            dp[0][0] = 1
        for i in range(rows):
            for j in range(cols):
                x = i
                y = j
                if obstacleGrid[i][j] == 0:
                    if x > 0 and y > 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    elif x > 0:
                        dp[i][j] = dp[i-1][j]
                    elif y > 0:
                        dp[i][j] = dp[i][j-1]
        return dp[rows-1][cols-1]

