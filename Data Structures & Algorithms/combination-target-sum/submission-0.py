class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        s = 0

        def dfs(start, s):
            if s == target:
                res.append(path.copy())
                return

            if s > target:
                return

            for i in range(start, len(nums)):
                s += nums[i]
                path.append(nums[i])
                dfs(i, s)
                path.pop()
                s -= nums[i]

        dfs(0, 0)
        return res