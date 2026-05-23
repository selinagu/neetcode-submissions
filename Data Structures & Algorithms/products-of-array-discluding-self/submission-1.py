class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]
        product = 1
        left = 1
        right = 1

        for i in range(1, len(nums)):
            left *= nums[i-1]
            products.append(left)

        for i in range(1, len(nums)):
            right *= nums[len(nums) - i]
            products[len(nums) - i - 1] *= right

        return products