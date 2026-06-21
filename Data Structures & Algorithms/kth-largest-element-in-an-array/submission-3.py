class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(l, r):
            i = l
            pivot = nums[r]
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[r] = nums[r], nums[i]
            return i

        L, R = 0, len(nums) - 1
        while L <= R:
            idx = quickselect(L, R)
            if idx == k:
                return nums[k]
            elif idx < k:
                L = idx + 1
            else:
                R = idx - 1