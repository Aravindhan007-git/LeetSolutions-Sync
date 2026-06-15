# Power of Three

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-three` |
| Topics | Math, Recursion |
| Solved | 2026-06-15 |
| Runtime | 9 ms (beats 51.42210000000003%) |
| Memory | 19.3 MB (beats 62.0065%) |

## Problem Statement

Given an integer `n`, return _`true` if it is a power of three. Otherwise, return `false`_.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.

 

**Example 1:**

**Input:** n = 27
**Output:** true
**Explanation:** 27 = 33

**Example 2:**

**Input:** n = 0
**Output:** false
**Explanation:** There is no x where 3x = 0.

**Example 3:**

**Input:** n = -1
**Output:** false
**Explanation:** There is no x where 3x = (-1).

 

**Constraints:**

	- `-231 <= n <= 231 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## Solutions

```Python3
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n%3==0:
            n//=3
        return n==1
```
