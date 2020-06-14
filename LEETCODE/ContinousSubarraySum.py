'''
Given a list of non-negative numbers and a target integer k,
write a function to check if the array has a continuous
subarray of size at least 2 that sums up to a multiple of k,
that is, sums up to n*k where n is also an integer.
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            exist_two_zero = False
            count = 0
            for i in range(len(nums)):
                x = nums[i]
                if x == 0:
                    if count == 0:
                        count += 1
                    else:
                        if nums[i-1] == 0:
                            count += 1
                if count >= 2:
                    exist_two_zero = True
                    break
            if exist_two_zero:
                return True
            else:
                return False
        running_sum = [0]
        for i in range(len(nums)):
            running_sum.append(running_sum[-1] + nums[i])
        is_exist = False
        for i in range(len(nums)):
            sub = running_sum[i]
            for j in range(i+2, len(running_sum)):
                if (running_sum[j]-sub)%k == 0:
                    is_exist = True
                    break
            if is_exist:
                break
        return is_exist