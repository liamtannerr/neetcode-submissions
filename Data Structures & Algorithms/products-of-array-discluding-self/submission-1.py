class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        preProduct = 1

        for i in range(len(nums)):
            prefix[i] = preProduct
            preProduct *= nums[i];
        
        postProduct = 1
        for i in reversed(range(len(nums))):
            suffix[i] = postProduct
            postProduct *= nums[i];

        res = []
        for i in range(len(nums)):
            res.append(suffix[i] * prefix[i])

        return res
