class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            if not i == 0:
                if nums[i] == nums[i - 1]:
                    continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if not j == i + 1:
                    if nums[j] == nums[j - 1]:
                        j += 1
                        continue
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1

        return res



        