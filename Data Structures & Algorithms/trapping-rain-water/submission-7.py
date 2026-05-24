class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        left_max = height[0]
        right_max = height[n - 1]
        area = 0

        for i in range(n):
            left_max = max(left_max, height[i])
            leftMax[i] = left_max

        for i in range(n-1, -1, -1):
            right_max = max(right_max, height[i])
            rightMax[i] = right_max

        for i in range(n):
            area += min(leftMax[i], rightMax[i]) - height[i]

        return area