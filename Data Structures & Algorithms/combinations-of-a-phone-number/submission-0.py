class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        represent = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z'),
        }

        if not digits:
            return []
            
        res = []
        path = ''

        def dfs(pos):
            nonlocal path

            if len(path) == len(digits):
                res.append(path)
                return

            digit = digits[pos]
            for i in range(len(represent[digit])): 
                path += represent[digit][i]
                dfs(pos + 1)
                path = path[:-1]

        dfs(0)

        return res