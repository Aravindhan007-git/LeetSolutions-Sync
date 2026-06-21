# Valid Anagram

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-valid-anagram` |
| Topics | String, Hash Table, Sorting |
| Solved | 2026-06-21 |
| Runtime | 19 ms (beats 15.995200000000025%) |
| Memory | 20.2 MB (beats 18.0437%) |

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

**Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

 

**Constraints:**

	- `1 <= s.length, t.length <= 5 * 104`

	- `s` and `t` consist of lowercase English letters.

 

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solutions

```Python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        else:
            return False
```
