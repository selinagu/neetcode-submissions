class Solution:
    def isValidHelper(self, group: List[str]) -> bool:
        visited = set()
        for item in group:
            if item in visited:
                return False
            if item != '.':
                visited.add(item)
        return True 

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidHelper(board[i]):
                return False

        for i in range(9):
            group = []
            for j in range(9):
                group.append(board[j][i])
            if not self.isValidHelper(group):
                return False

        group1 = []
        group2 = []
        group3 = []
        for i in range(3):
            
            for j in range(3):
                group1.append(board[i][j])
            for j in range(3, 6):
                group2.append(board[i][j])
            for j in range(6, 9):
                group3.append(board[i][j])
            if not self.isValidHelper(group1):
                return False
            if not self.isValidHelper(group2):
                return False
            if not self.isValidHelper(group3):
                return False

        group4 = []
        group5 = []
        group6 = []
        for i in range(3, 6):

            for j in range(3):
                group4.append(board[i][j])
            for j in range(3, 6):
                group5.append(board[i][j])
            for j in range(6, 9):
                group6.append(board[i][j])
            if not self.isValidHelper(group4):
                return False
            if not self.isValidHelper(group5):
                return False
            if not self.isValidHelper(group6):
                return False

        group7 = []
        group8 = []
        group9 = []
        for i in range(6, 9):
        
            for j in range(3):
                group7.append(board[i][j])
            for j in range(3, 6):
                group8.append(board[i][j])
            for j in range(6, 9):
                group9.append(board[i][j])
            if not self.isValidHelper(group1):
                return False
            if not self.isValidHelper(group2):
                return False
            if not self.isValidHelper(group3):
                return False

        return True