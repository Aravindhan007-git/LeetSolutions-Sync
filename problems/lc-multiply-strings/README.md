# Multiply Strings

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-multiply-strings` |
| Topics | Math, String, Simulation |
| Solved | 2026-06-25 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.1 MB (beats 93.7283%) |

## Problem Statement

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

**Example 1:**

**Input:** num1 = "2", num2 = "3"
**Output:** "6"
**Example 2:**

**Input:** num1 = "123", num2 = "456"
**Output:** "56088"

 

**Constraints:**

	- `1 <= num1.length, num2.length <= 200`

	- `num1` and `num2` consist of digits only.

	- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

## Solutions

```Python3
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))
```
