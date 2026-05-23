class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0

        for i in range(1, len(heights)):
            for j in range(i):
                width = i - j
                height = min(heights[i], heights[j])
                area = width * height
                maxarea = max(area, maxarea)

        return maxarea