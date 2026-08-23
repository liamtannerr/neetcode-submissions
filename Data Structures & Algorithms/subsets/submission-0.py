class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        self.subset = []

        def dfs(i):
            if i >= len(nums):
                self.res.append(self.subset.copy())
                return
            
            self.subset.append(nums[i])
            dfs(i + 1)

            self.subset.pop()
            dfs(i + 1)

        dfs(0)
        return self.res