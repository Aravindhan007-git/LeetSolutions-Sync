class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.']*n for _ in range(n)]
        res = []

        def safe(r,c):
            for i in range(n):
                if board[i][c] == 'Q':
                    return False

            i = r-1
            j = c-1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j-=1
            i = r-1
            j = c+1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j+=1
            return True
        
        def solve(r):
            if r == n:
                x = []
                for i in range(n):
                    x.append("".join(board[i]))
                res.append(x)
                return
            for c in range(n):
                if safe(r,c):
                    board[r][c] = 'Q'
                    solve(r+1)
                    board[r][c] = '.'
        solve(0)
        return res