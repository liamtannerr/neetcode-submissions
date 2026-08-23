class Solution:
    def findMin(self, nums: List[int]) -> int:

        minVal = 1000
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break
            cur = (l + r) // 2
            minVal = min(minVal, nums[cur])
            if nums[cur] >= nums[l]:
                l = cur + 1
            else:
                r = cur - 1

        return minVal
        