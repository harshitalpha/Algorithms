'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  
During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  
Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?
'''
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0.0] * (N+W+1)
        for i in range(K, N+1):
            dp[i] = 1.0
        
        S = min(N-K+1, W)
        for k in range(K-1,-1,-1):
            dp[k] = S/float(W)
            S = S + (dp[k] - dp[k+W])
        return dp[0]
