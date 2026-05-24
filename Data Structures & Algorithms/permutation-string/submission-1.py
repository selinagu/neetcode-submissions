class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = {}
        for i in range(26):
            freq1[i] = 0
        for s in s1:
            freq1[ord(s) - ord('a')] += 1

        freq2 = {}
        for i in range(26):
            freq2[i] = 0
        for t in s2[:len(s1)]:
            freq2[ord(t) - ord('a')] += 1

        if freq1 == freq2:
            return True

        for i in range(len(s1), len(s2)):
            freq2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            freq2[ord(s2[i]) - ord('a')] += 1
            if freq2 == freq1:
                return True

        return False