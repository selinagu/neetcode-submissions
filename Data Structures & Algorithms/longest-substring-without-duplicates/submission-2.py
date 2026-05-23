class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        max_length = 0
        for ch in s:
            if ch in substring:
                max_length = max(max_length, len(substring))
                pos = substring.rfind(ch)
                substring = substring[pos+1:] + ch
            else:
                substring += ch

        return max(max_length, len(substring))