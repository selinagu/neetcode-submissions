class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        zero_pos = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_pos.append(i)
        
        num_zero = len(zero_pos)
        if num_zero > 1:
            return result

        elif num_zero == 1:
            i = zero_pos[0]
            pro = 1
            for num in nums:
                if num != 0:
                    pro *= num
            result[i] = pro
            return result

        else:
            product = 1
            for num in nums:
                product *= num
            for i in range(len(nums)):
                result[i] = product // nums[i]
            return result