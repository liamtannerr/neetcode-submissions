class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        curMax = 0

        for num in nums:
            if num - 1 in s:
                continue
            i = num
            curLen = 0
            while i in s:
                curLen += 1
                i += 1
            curMax = max(curMax, curLen)

        return curMax