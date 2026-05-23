class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            comple = target - nums[i]
            if comple in visited:
                return [visited[comple], i]
            visited[nums[i]] = i