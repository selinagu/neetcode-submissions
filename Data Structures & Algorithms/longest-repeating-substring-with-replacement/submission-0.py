class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        substring = ''
        max_length = 0

        for right in range(len(s)):
            substring += s[right]
            freq = {}
            for char in substring:
                freq[char] = freq.get(char, 0) + 1
            max_freq = max(freq.values())
            while (len(substring) - max_freq) > k:
                left += 1
                substring = substring[1:]
                
            max_length = max(len(substring), max_length)

        return max_length
