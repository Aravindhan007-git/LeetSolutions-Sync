# Reverse Integer

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-reverse-integer` |
| Topics | Math |
| Solved | 2026-05-04 |
| Runtime | 44 ms (beats 68.31060000000002%) |
| Memory | 19.3 MB (beats 8.722100000000005%) |

## Problem Statement

Given a signed 32-bit integer `x`, return `x`_ with its digits reversed_. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

 

**Example 1:**

**Input:** x = 123
**Output:** 321

**Example 2:**

**Input:** x = -123
**Output:** -321

**Example 3:**

**Input:** x = 120
**Output:** 21

 

**Constraints:**

	- `-231 <= x <= 231 - 1`

## Solutions

```Python3
class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        rev=0
        x=abs(x)
        while x>0:
            d=x%10
            rev=rev*10+d
            x//=10
        rev=rev*sign
        if rev>(2**31)-1 or rev<(-2**31):
            return 0
        else :
            return rev
```
