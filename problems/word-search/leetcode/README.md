# Word Search

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-word-search` |
| Topics | Grid, Array, String, Backtracking, Depth-First Search, Matrix |
| Solved | 2026-09-01 |
| Runtime | 5321 ms (beats 11.103400000002551%) |
| Memory | 19.4 MB (beats 83.8365%) |

## Problem Statement

Given an `m x n` grid of characters `board` and a string `word`, return `true` _if_ `word` _exists in the grid_.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

**Example 1:**

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
**Output:** true

**Example 2:**

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
**Output:** true

**Example 3:**

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
**Output:** false

 

**Constraints:**

	- `m == board.length`

	- `n = board[i].length`

	- `1 <= m, n <= 6`

	- `1 <= word.length <= 15`

	- `board` and `word` consists of only lowercase and uppercase English letters.

 

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

## Solutions

```Python3
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
            
```
