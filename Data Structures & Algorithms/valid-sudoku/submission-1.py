class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        square = defaultdict(list)

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur in row[i]:
                    return False
                elif cur != '.':
                    row[i].append(cur)

                if cur in col[j]:
                    return False
                elif cur != '.':
                    col[j].append(cur)

                if cur in square[(i//3, j//3)]:
                    return False
                elif cur != '.':
                    square[(i//3, j//3)].append(cur)
        
        return True