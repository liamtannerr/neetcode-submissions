class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(path, seen):
            if len(path) == len(nums):
                self.res.append(path[:])
                return
            for i in range(len(nums)):
                if not seen[i]:
                    seen[i] = True
                    path.append(nums[i])
                    dfs(path, seen)
                    path.pop()         # undo
                    seen[i] = False     # undo

        dfs([], [False] * len(nums))
        return self.res