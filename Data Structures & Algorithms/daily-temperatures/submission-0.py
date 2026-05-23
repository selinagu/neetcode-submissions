class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []
        for i in range(n-1):
            found = False
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    found = True
                    break
            if not found:
                res.append(0)
        res.append(0)
        return res