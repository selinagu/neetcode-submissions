class Solution:
    def palindrome(self, sub):
        for i in range(len(sub) // 2):
            if sub[i] != sub[len(sub) - i - 1]:
                return False

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(start):
            if start == len(s):
                res.append(path.copy())
                return

            for i in range(start, len(s)):
                substring = s[start: i + 1]
                if self.palindrome(substring):
                    path.append(substring)
                    dfs(i + 1)
                    path.pop()

        dfs(0)

        return res