class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elt = float('-inf')
        for i in range(k):
            if nums[i] > max_elt:
                max_elt = nums[i]
                max_pos = i
        res = [max_elt]
        left = 1
        right = k
        
        while right < len(nums):
            max_pos -= 1
            if max_pos < 0:
                max_elt = float('-inf')
                for i in range(k):
                    if nums[left+i] > max_elt:
                        max_elt = nums[left+i]
                        max_pos = i
            elif nums[right] > max_elt:
                max_elt = nums[right]
                max_pos = k-1
            res.append(max_elt)
            left += 1
            right += 1

        return res