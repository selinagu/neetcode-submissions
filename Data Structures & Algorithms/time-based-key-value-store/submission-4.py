class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if self.timeMap[key]:
            times = sorted(self.timeMap[key].keys())
            l = 0
            r = len(times)
            while l < r:
                m = (l + r) // 2
                if times[m] > timestamp:
                    r = m
                else:
                    l = m + 1

            return self.timeMap[key][times[l - 1]] if l > 0 else ''

        return ''
