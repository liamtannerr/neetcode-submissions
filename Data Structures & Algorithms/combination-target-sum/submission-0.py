class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res = []

        def dfs(i, path, total):
            if total == target:
                self.res.append(path.copy())
                return
            elif i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            dfs(i, path, total + nums[i])
            path.pop()
            dfs(i + 1, path, total)

        dfs(0, [], 0)
        return self.res

