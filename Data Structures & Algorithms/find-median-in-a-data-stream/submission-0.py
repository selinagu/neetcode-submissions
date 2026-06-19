class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.nums, num)
        self.length += 1

    def findMedian(self) -> float:
        n = len(self.nums)
        heap = self.nums.copy()
        m = (n - 1) // 2

        for _ in range(m):
            heapq.heappop(heap)

        if n % 2 == 1:
            return heapq.heappop(heap)

        else:
            num1 = heapq.heappop(heap)
            num2 = heapq.heappop(heap)
            return (num1 + num2) / 2
        