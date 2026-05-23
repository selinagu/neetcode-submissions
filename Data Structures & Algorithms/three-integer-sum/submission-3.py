class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        res = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and sort_nums[i] == sort_nums[i-1]:
                continue
            sum_two = - sort_nums[i]
            j = i + 1
            k = n - 1

            while j < k:
                if j > i + 1 and sort_nums[j] == sort_nums[j-1]:
                    j += 1
                    continue
                if k < n - 1 and sort_nums[k] == sort_nums[k+1]:
                    k -= 1
                    continue
                if sort_nums[j] + sort_nums[k] == sum_two:
                    res.append([sort_nums[i], sort_nums[j], sort_nums[k]])
                    j += 1
                    k -= 1
                elif sort_nums[j] + sort_nums[k] < sum_two:
                    j += 1
                else:
                    k -= 1

        return res