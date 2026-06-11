# Rotate String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-rotate-string` |
| Topics | String, String Matching |
| Solved | 2026-06-11 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 52.36439999999998%) |

## Problem Statement

Given two strings `s` and `goal`, return `true` _if and only if_ `s` _can become_ `goal` _after some number of **shifts** on_ `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

	- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

 

**Example 1:**

**Input:** s = "abcde", goal = "cdeab"
**Output:** true
**Example 2:**

**Input:** s = "abcde", goal = "abced"
**Output:** false

 

**Constraints:**

	- `1 <= s.length, goal.length <= 100`

	- `s` and `goal` consist of lowercase English letters.

## Solutions

```Python3
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            rotated=s[i:]+s[:i]
            if rotated == goal:
                return True
        return False
```
