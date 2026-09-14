import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        p, l, r = 0, 0, len(nums) - 1

        while l <= r:
            i, p = l, l
            pivot_idx = random.randint(l,r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            partition = nums[r]
            while i < r:
                if partition > nums[i]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1      
                i += 1
            nums[r], nums[p] = nums[p], nums[r]
            if (p == len(nums) - k):
                return nums[p]
            elif p < len(nums) - k:
                l = p + 1
            else:
                r = p -1

        return nums[p]
