class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        self.res = []
        self.subset = []
        nums.sort()

        def dfs(idx):
            if idx >= len(nums):
                self.res.append(self.subset.copy())
                return
            
            self.subset.append(nums[idx])
            dfs(idx + 1)
            self.subset.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1)

        dfs(0)  
        return self.res      