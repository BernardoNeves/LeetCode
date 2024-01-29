class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def check_unique(arr):
            for a in arr:
                if a != "." and arr.count(a) > 1:
                    return False
            return True

        def check_row(row):
            return check_unique(board[row])

        def check_col(col):
            return check_unique([board[row][col] for row in range(9)])

        def check_square(row, col):
            return check_unique(
                [board[row + i][col + j] for i in range(3) for j in range(3)]
            )

        for i in range(9):
            if not check_row(i) or not check_col(i):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_square(i, j):
                    return False
        return True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_square(i, j):
                    return False
        return True
