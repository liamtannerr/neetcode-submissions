class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set()
        curMax = 0

        for num in nums:
            s.add(num)

        for num in nums:
            i = num
            curLen = 0
            while i in s:
                curLen += 1
                i += 1
            curMax = max(curMax, curLen)

        return curMax