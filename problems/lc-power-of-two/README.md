# Power of Two

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-two` |
| Topics | Math, Bit Manipulation, Recursion |
| Solved | 2026-06-23 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 53.103899999999996%) |

## Problem Statement

Given an integer `n`, return _`true` if it is a power of two. Otherwise, return `false`_.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

 

**Example 1:**

**Input:** n = 1
**Output:** true
**Explanation: **20 = 1

**Example 2:**

**Input:** n = 16
**Output:** true
**Explanation: **24 = 16

**Example 3:**

**Input:** n = 3
**Output:** false

 

**Constraints:**

	- `-231 <= n <= 231 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## Solutions

```Python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while 1:
            if 2**i==n:
                return True
            if 2**i>n:
                return False
            i+=1
```
