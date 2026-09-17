import math

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        memo = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            if not(memo[i] == -1):
                return memo[i]
            memo[i] = max(nums[i] + dfs(i + 2), dfs( i + 1))
            return memo[i]
        
        res = dfs(0)

        return res
