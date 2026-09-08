class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums_seen = set()

        for num in nums:
            if num in nums_seen:
                return num
            nums_seen.add(num)

        return -1


        
        