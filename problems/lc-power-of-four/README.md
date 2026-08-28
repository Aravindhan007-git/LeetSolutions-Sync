# Power of Four

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-four` |
| Topics | Math, Bit Manipulation, Recursion |
| Solved | 2026-08-28 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.4 MB (beats 24.78099999999999%) |

## Problem Statement

Given an integer `n`, return _`true` if it is a power of four. Otherwise, return `false`_.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4x`.

 

**Example 1:**

**Input:** n = 16
**Output:** true
**Example 2:**

**Input:** n = 5
**Output:** false
**Example 3:**

**Input:** n = 1
**Output:** true

 

**Constraints:**

	- `-231 <= n <= 231 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## Solutions

```Python3
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        while n%4==0:
            n//=4
        return n==1
```
