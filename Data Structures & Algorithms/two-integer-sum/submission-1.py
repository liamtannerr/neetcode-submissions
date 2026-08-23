class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in count.keys()):
                return[count[complement], i]
            count[nums[i]] = i

        return []

        