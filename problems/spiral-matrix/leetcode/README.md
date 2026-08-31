# Spiral Matrix

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-spiral-matrix` |
| Topics | Array, Matrix, Simulation |
| Solved | 2026-08-31 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.1 MB (beats 99.1981%) |

## Problem Statement

Given an `m x n` `matrix`, return _all elements of the_ `matrix` _in spiral order_.

 

**Example 1:**

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,2,3,6,9,8,7,4,5]

**Example 2:**

**Input:** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
**Output:** [1,2,3,4,8,12,11,10,9,5,6,7]

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 10`

	- `-100 <= matrix[i][j] <= 100`

## Solutions

```Python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        r=len(matrix)
        c=len(matrix[0])
        top=0
        left=0
        bottom=r-1
        right=c-1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom
                ,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            
        return res
```
