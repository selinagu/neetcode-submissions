class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l1 = len(nums1)
        l2 = len(nums2)
        total_left = (l1 + l2) // 2
        left = -1
        right = l1 - 1

        while left <= right:
            i = (left + right) // 2
            j = total_left - i - 2
            nums1_left = float('-inf') if i < 0 else nums1[i]
            nums1_right = float('inf') if i > l1 - 2 else nums1[i + 1]

            nums2_left = float('-inf') if j < 0 else nums2[j]
            nums2_right = float('inf') if j > l2 - 2 else nums2[j + 1]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (l1 + l2) % 2 == 1:
                    return min(nums1_right, nums2_right)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1