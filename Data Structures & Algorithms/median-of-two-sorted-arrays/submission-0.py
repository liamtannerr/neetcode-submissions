class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        size = len(nums1) + len(nums2)
        target = size // 2
        p1, p2 = 0, 0
        curr = 0

        for _ in range(target + 1):
            prev = curr
            if p1 < len(nums1) and (p2 == len(nums2) or nums1[p1] < nums2[p2]):
                curr = nums1[p1]
                p1 += 1
            else:
                curr = nums2[p2]
                p2 += 1

        if size % 2 == 0:
            return (curr + prev) / 2.0
        else:
            return float(curr)

