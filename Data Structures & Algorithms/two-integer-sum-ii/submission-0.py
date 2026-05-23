class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers) - 1
        num1 = numbers[idx1]
        num2 = numbers[idx2]

        while num1 < num2:
            if num1 + num2 == target:
                return [idx1 + 1, idx2 + 1]
            elif num1 + num2 > target:
                idx2 -= 1
                num2 = numbers[idx2]
            else:
                idx1 += 1
                num1 = numbers[idx1]


