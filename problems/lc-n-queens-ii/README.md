# N-Queens II

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-n-queens-ii` |
| Topics | Backtracking, Algorithm X |
| Solved | 2026-09-16 |
| Solve Time | 35m 58s |
| Runtime | 31 ms (beats 9.522900000000016%) |
| Memory | 19.5 MB (beats 9.896999999999982%) |

## Problem Statement

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _the number of distinct solutions to the **n-queens puzzle**_.

 

**Example 1:**

**Input:** n = 4
**Output:** 2
**Explanation:** There are two distinct solutions to the 4-queens puzzle as shown.

**Example 2:**

**Input:** n = 1
**Output:** 1

 

**Constraints:**

	- `1 <= n <= 9`

## Solutions

```Python3
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.']*n for _ in range(n)]
        res = []
        co = 0
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
            nonlocal co
            if r == n:
                co+=1
                return
            for c in range(n):
                if safe(r,c):
                    board[r][c] = 'Q'
                    solve(r+1)
                    board[r][c] = '.'
        solve(0)
        return co
```
