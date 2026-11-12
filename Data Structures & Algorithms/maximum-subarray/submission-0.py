# We track 2 sums, a global maximum and the max of the current subarray that we are evaluating
# We iterate through the array and decide with each step whether we are going to extend the current subarray and if not, we start a new subarray
# We continue extending as long as cursum is greater than 0, if it ever becomes less we know that we do not need to care about what came before and we restart the subarray.

import math

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        res = -math.inf
        cur_sum = 0

        for num in nums:
            cur_sum += num
            res = max(res, cur_sum)

            if cur_sum <= 0:
                cur_sum = 0

        return res
        