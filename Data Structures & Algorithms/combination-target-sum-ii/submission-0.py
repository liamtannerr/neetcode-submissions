class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        self.res = []

        def dfs(idx, path, total):
            if total == target:
                self.res.append(path.copy())
                return
            if idx >= len(candidates) or total > target:
                return

            path.append(candidates[idx])
            dfs(idx + 1, path, total + candidates[idx])

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1

            path.pop()
            dfs(idx + 1, path, total)


        dfs(0, [], 0)
        return self.res

        


        