class Solution:
    def maxArea(self, heights: List[int]) -> int:

        Max = 0

        left = 0
        right = len(heights) - 1

        while left < right:

            area = (right - left) * min(heights[right], heights[left])
            Max = max(Max, area)

            if heights[right] > heights[left]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                right -= 1
                left += 1

        return Max

        