class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_map = defaultdict(int)
        for task in tasks:
            tasks_map[task] += 1

        heap = []
        for task, num in tasks_map.items():
            heapq.heappush(heap, (-num, task))

        t = 0
        store = deque()
        while heap or store:
            t += 1
            if heap:
                num_neg, task = heapq.heappop(heap)
                if num_neg < -1:
                    store.append((num_neg + 1, task, t))

            if store:
                _, _, time = store[0]
                if time + n == t:
                    num_neg, task, _ = store.popleft()
                    heapq.heappush(heap, (num_neg, task))

        return t