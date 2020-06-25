'''
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.
'''

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        
        dp = {}
        def solve(m, n, moves, i, j):
            if i < 0 or i >= m:
                return 0
            if j < 0 or j >= n:
                return 0
            if moves == 1:
                if m == 1 and n == 1:
                    return 4
                elif m == 1:
                    if j == 0 or j == n-1:
                        return 3
                    return 2
                elif n ==1:
                    if i == 0 or i == m-1:
                        return 3
                    return 2
                else:
                    if (i==0 and j==0) or (i==0 and j==n-1) or (i==m-1 and j==0) or (i==m-1 and j==n-1):
                        return 2
                    elif i == 0 or i == m-1 or j == 0 or j == n-1:
                        return 1
                    else:
                        return 0
            if (i,j,moves) in dp:
                return dp[(i,j,moves)]
            else:
                x = solve(m,n,moves-1,i-1,j)
                y = solve(m,n,moves-1,i,j-1)
                z = solve(m,n,moves-1,i+1,j)
                w = solve(m,n,moves-1,i,j+1)
                print(x,y,z,w)
                dp[(i,j,moves)] = x+y+z+w
                return dp[(i,j,moves)]
        
        ans = 0
        for move in range(1,N+1):
            ans = ans + solve(m,n,move,i,j)
            print(ans)
        return ans%1000000007
            
                    
