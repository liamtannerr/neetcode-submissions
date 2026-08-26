import math

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        elif n == 3:
            return max(nums[0] + nums[2], nums[1])

        self.memo = [-1] * n

        def check_paths(index):
            if index > len(nums) - 1:
                return 0
            
            if not(self.memo[index] == -1):
                return self.memo[index]

            cur_max = max(nums[index] + check_paths(index + 2), check_paths(index + 1))
            self.memo[index] = cur_max
            return cur_max

        return check_paths(0)