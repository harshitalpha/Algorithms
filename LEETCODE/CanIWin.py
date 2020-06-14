'''
In the "100 game," two players take turns adding, to a running total,
any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement
until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal,
determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger
will not be larger than 20 and desiredTotal will not be larger than 300.
'''


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if ((maxChoosableInteger + 1) * maxChoosableInteger / 2) < desiredTotal:
            print("Hello")
            return False
        memo = {}

        def solve(nums, target):
            if nums[-1] >= target:
                return True
            if nums in memo:
                return memo[nums]
            else:
                for i in range(len(nums)):
                    if not solve(nums[:i] + nums[i + 1:], target - nums[i]):
                        memo[nums] = True
                        return True
                memo[nums] = False
                return False

        nums = tuple(range(1, maxChoosableInteger + 1))
        print(nums)
        return solve(nums, desiredTotal)
