class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for i in range(len(s)):
            if s[i] in pairs:
                stack.append(s[i])
            elif not stack:
                return False
            else:
                left = stack.pop()
                if s[i] != pairs[left]:
                    return False

        return not stack