'''
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array.
Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.
'''

class Solution:
    def LongestContigiousSubarray(self, a):
        # KADEANS ALGO
        size = len(a)
        max_so_far = 0
        max_ending_here = 0

        for i in range(0, size):
            max_ending_here = max_ending_here + a[i]
            if max_ending_here < 0:
                max_ending_here = 0

            # Do not compare for all elements. Compare only
            # when  max_ending_here > 0
            elif (max_so_far < max_ending_here):
                max_so_far = max_ending_here

        return max_so_far

    def kConcatenationMaxSum(self, arr, k: int) -> int:
        is_all_pos = 1
        for i in arr:
            if i < 0:
                is_all_pos = 0
        if is_all_pos == 1:
            return (sum(arr) * k) % 1000000007
        else:
            modified_arr = arr + arr
            x = self.LongestContigiousSubarray(modified_arr)
            s = sum(arr)
            if s < 0:
                return x % 1000000007
            else:
                return (x + (k - 2) * s) % 1000000007
