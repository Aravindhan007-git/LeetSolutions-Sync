# Spiral Matrix II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-spiral-matrix-ii` |
| Topics | Array, Matrix, Simulation |
| Solved | 2026-08-31 |
| Runtime | 43 ms (beats 0.6920999999999966%) |
| Memory | 19.5 MB (beats 11.124299999999998%) |

## Problem Statement

Given a positive integer `n`, generate an `n x n` `matrix` filled with elements from `1` to `n2` in spiral order.

 

**Example 1:**

**Input:** n = 3
**Output:** [[1,2,3],[8,9,4],[7,6,5]]

**Example 2:**

**Input:** n = 1
**Output:** [[1]]

 

**Constraints:**

	- `1 <= n <= 20`

## Solutions

```Python3
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums=[[0]*n for _ in range(n)]
        top=0
        left=0
        bottom=n-1
        right=n-1
        a=1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                nums[top][i]=a
                a+=1
            top+=1
            for i in range(top,bottom+1):
                nums[i][right]=a
                a+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    nums[bottom][i]=a
                    a+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    nums[i][left]=a
                    a+=1
                left+=1
        return nums
```
