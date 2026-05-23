from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        sorted_nums = dict(sorted(count.items(), key = lambda item: item[1], reverse = True))
        topk = list(sorted_nums.keys())[:k]

        return topk