class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        if not heights:
            return 0

        s = []
        max_area = 0

        for i in range(len(heights)):
            top_idx = i
            while s and s[-1][1] > heights[i]:
                top_idx, top_height = s.pop()
                max_area = max(max_area, top_height * (i - top_idx))

            s.append((top_idx, heights[i]))

        for i, height in s:
            max_area = max(max_area, height * (len(heights) - i))

        return max_area