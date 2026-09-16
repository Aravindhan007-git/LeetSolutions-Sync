# N-Queens

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-n-queens` |
| Topics | Array, Backtracking, Algorithm X |
| Solved | 2026-09-16 |
| Solve Time | 35m 58s |
| Runtime | 32 ms (beats 15.220299999999988%) |
| Memory | 19.7 MB (beats 70.73230000000001%) |

## Problem Statement

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _all distinct solutions to the **n-queens puzzle**_. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

 

**Example 1:**

**Input:** n = 4
**Output:** [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
**Explanation:** There exist two distinct solutions to the 4-queens puzzle as shown above

**Example 2:**

**Input:** n = 1
**Output:** [["Q"]]

 

**Constraints:**

	- `1 <= n <= 9`

## Solutions

```Python3
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
```
