class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_length = 1
                current = num
                while current + 1 in nums_set:
                    cur_length += 1
                    current += 1
                max_length = max(max_length, cur_length)
                
        return max_length