class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        max_length = 1
        cur_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cur_length += 1

            elif nums[i] == nums[i-1]:
                continue

            else:
                max_length = max(max_length, cur_length)
                cur_length = 1

        return max(max_length, cur_length)