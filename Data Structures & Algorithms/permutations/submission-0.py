class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = []
        element = nums.pop()
        output = self.permute(nums)
        
        for out in output:
            for i in range(len(out)):
                new_out = out.copy()
                new_out.insert(i, element)
                res.append(new_out)
            
            res.append(out + [element])

        return res