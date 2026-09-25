class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]
        elif n <= 3:
            return max(nums)

        end = nums[1:]
        start = nums[:n-1]
        memo_end = [0] * (n-1)
        memo_start = [0] * (n-1)

        memo_end[0], memo_start[0] = end[0], start[0]
        memo_end[1], memo_start[1] = max(end[0], end[1]), max(start[0], start[1])

        for i in range(2, n-1):
            memo_end[i] = max(memo_end[i-1], memo_end[i-2] + end[i])
            memo_start[i] = max(memo_start[i-1], memo_start[i-2] + start[i])

        return max(memo_end[n-2], memo_start[n-2])