class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        for i in range(m - n + 1):
            sub = s2[i: i+n]
            if sorted(s1) == sorted(sub):
                return True

        return False
