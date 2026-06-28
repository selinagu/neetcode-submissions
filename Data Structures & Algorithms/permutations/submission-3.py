class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.mask = 0
        self.backtrack([], nums)
        return self.res

    def backtrack(self, perm: List[int], nums: List[int]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not (self.mask & (1 << i)):
                perm.append(nums[i])
                self.mask ^= (1 << i)
                self.backtrack(perm, nums)
                self.mask ^= (1 << i)
                perm.pop()