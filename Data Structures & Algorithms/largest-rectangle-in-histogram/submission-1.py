class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                pos = stack.pop()
                if stack:
                    left = stack[-1] + 1
                else:
                    left = 0
                right = i - 1
                area = heights[pos] * (right - left + 1)
                max_area = max(area, max_area)
            stack.append(i)

        for i in range(len(stack) - 1, -1, -1):
            right = len(heights) - 1
            pos = stack.pop()
            if stack:
                left = stack[-1] + 1
            else:
                left = 0
            area = heights[pos] * (right - left + 1)
            max_area = max(area, max_area)

        return max_area
            