class Solution:

    def checkForRow(self, board: List[List[str]]) -> bool:
        for i in range(9):
            arr = [0] * 9
            for j in range(9):
                if board[i][j] != '.':
                    if arr[int(board[i][j])-1] == 1:
                        return False
                    else:
                        arr[int(board[i][j])-1] = 1
        return True

    def checkForColumns(self, board: List[List[str]]) -> bool:
        for j in range(9):
            arr = [0] * 9
            for i in range(9):
                if board[i][j] != '.':
                    if arr[int(board[i][j])-1] == 1:
                        return False
                    else:
                        arr[int(board[i][j])-1] = 1
        return True

    def checkForBox(self, board: List[List[str]]) -> bool:
        for b in range(9):
            arr = [0] * 9
            for i in range((b//3)*3,((b//3)*3)+3):
                for j in range((b%3)*3,((b%3)*3)+3):
                    if board[i][j] != '.':
                        if arr[int(board[i][j])-1] == 1:
                            return False
                        else:
                            arr[int(board[i][j])-1] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkForRow(board) and self.checkForColumns(board) and self.checkForBox(board)