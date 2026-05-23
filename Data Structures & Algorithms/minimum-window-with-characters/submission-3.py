class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        if not s or not t:
            return ''

        count_t = Counter(t)
        min_length = float('inf')
        best_sub = ''
        left = 0
        right = 0

        while right < len(s):
            sub = s[left: right+1]
            freq = Counter(sub)
            if freq >= count_t:
                while sub[0] not in t or freq[sub[0]] > count_t[sub[0]]:
                    freq[sub[0]] -= 1
                    sub = sub[1:]
                    left += 1
                length = len(sub)
                if length < min_length:
                    min_length = length
                    best_sub = sub
            right += 1

        return best_sub