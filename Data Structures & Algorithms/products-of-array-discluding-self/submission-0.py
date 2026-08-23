class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = 1

        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]

        product = 1

        for i in reversed(range(len(nums))):
            suffix[i] = product
            product *= nums[i]

        output = [1] * len(nums)

        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]

        return output
        