class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        visited = set()
        res = []

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if (nums_sort[i], nums_sort[j]) not in visited:
                    first = nums_sort[i]
                    second = nums_sort[j]
                    visited.add((first, second))
                    third = - first - second
                    if third in nums_sort[j+1:]:
                        res.append([first, second, third])

        return res