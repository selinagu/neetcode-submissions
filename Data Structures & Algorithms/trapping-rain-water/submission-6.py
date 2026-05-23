class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        left = height[0]
        right = height[n - 1]
        area = 0

        if n < 3:
            return 0

        while i < j:
            if height[i] < height[j]:
                if height[i] < left:
                    area += (left - height[i])
                else:
                    left = height[i]
                i += 1

            else:
                if height[j] < right:
                    area += (right - height[j])
                else:
                    right = height[j]
                j -= 1


        return area