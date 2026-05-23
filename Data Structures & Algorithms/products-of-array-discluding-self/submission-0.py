class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            products.append(product)
        return products