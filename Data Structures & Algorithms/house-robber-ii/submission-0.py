class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        n = len(nums) - 1

        memo_first = [-1] * n
        memo_last = [-1] * n

        def dfs(i, houses, memo):

            if i >= n:
                return 0
            
            if not(memo[i] == -1):
                return memo[i]

            memo[i] = max(houses[i] + dfs(i + 2, houses, memo), dfs(i + 1, houses, memo))
            return memo[i]

        first_house = nums[:n]
        last_house = nums[1:]

        return max(dfs(0, first_house, memo_first), dfs(0, last_house, memo_last))

        