class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        root = TrieNode()

        for word in words:
            cur = root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]

            cur.word = word

        res = set()
        visited = set()

        def dfs(row, col, cur):

            if row < 0 or row >= n or col < 0 or col >= m or (row, col) in visited:
                return 

            if board[row][col] not in cur.children:
                return

            letter = board[row][col]
            cur = cur.children[letter]
            visited.add((row, col))

            if cur.word:
                res.add(cur.word)

            dfs(row - 1, col, cur)
            dfs(row + 1, col, cur)
            dfs(row, col - 1, cur)
            dfs(row, col + 1, cur)

            visited.discard((row, col))

        for i in range(n):
            for j in range(m):
                dfs(i, j, root)

        return list(res)