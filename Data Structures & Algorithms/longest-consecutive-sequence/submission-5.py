class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        for num in nums:
            if num - 1 not in nums:
                cur_length = 1
                current = num
                while current + 1 in nums:
                    cur_length += 1
                    current += 1
                max_length = max(max_length, cur_length)
        return max_length