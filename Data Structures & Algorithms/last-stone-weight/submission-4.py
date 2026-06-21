class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            cur = stones.pop() - stones.pop()

            if cur > 0:
                left = 0
                right = len(stones)

                while left < right:
                    mid = (left + right) // 2

                    if stones[mid] < cur:
                        left = mid + 1
                    else:
                        right = mid

                pos = left
                stones.append(0)
                for i in range(len(stones) - 2, pos - 1, -1):
                    stones[i + 1] = stones[i]
                stones[pos] = cur

        if len(stones) == 1:
            return stones[0]

        return 0
