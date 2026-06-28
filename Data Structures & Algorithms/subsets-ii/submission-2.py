class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                idx = prev_idx
            else:
                idx = 0
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)

        return res