class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, path, cur_sum):
            if cur_sum > target or i >= len(nums):
                return
            elif cur_sum == target:
                res.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i, path, cur_sum + nums[i])
            path.pop()
            dfs(i + 1, path, cur_sum)

        dfs(0, [], 0)

        return res

