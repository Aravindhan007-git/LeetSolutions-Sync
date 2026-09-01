class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
        sol=[([0]*c) for i in range(r)]
        def solve(i,j,curr,sol,board):
            if curr==word:
                return True
            if i<0 or j<0 or i>=r or j>=c or sol[i][j]==1:
                return False 
            curr=curr+board[i][j]
            if curr==word:
                return True
            if len(curr)>=len(word):
                return False
            sol[i][j]=1
            if solve(i+1,j,curr,sol,board): return True
            if solve(i,j+1,curr,sol,board): return True
            if solve(i-1,j,curr,sol,board): return True
            if solve(i,j-1,curr,sol,board): return True
            sol[i][j]=0
            return False
        f=False
        for a in range(r):
            for b in range(c):
                if board[a][b]==word[0] and not f:
                    f=solve(a,b,"",sol,board)
        return f
            