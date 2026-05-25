class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        blocks = []
        res = []

        while i < len(nums) - k:
            blocks.append(nums[i: i+k])
            i += k
        blocks.append(nums[i:])

        leftMax = []
        rightMax = []
        for block in blocks:
            for i in range(len(block)):
                leftMax.append(max(block[:i+1]))
                rightMax.append(max(block[i:]))

        for i in range(len(nums) - k + 1):
            left_max = rightMax[i]
            right_max = leftMax[i+k-1]
            res.append(max(left_max, right_max))

        return res