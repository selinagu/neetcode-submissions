class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        fre = defaultdict(list)
        res = []

        for num in nums:
            count[num] += 1
        for num, cnt in count.items():
            fre[cnt].append(num)

        for i in range(len(nums), -1, -1):
            for num in fre[i]:
                res.append(num)
                if len(res) == k:
                    return res