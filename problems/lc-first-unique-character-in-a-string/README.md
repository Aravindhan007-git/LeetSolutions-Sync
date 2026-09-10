# First Unique Character in a String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-first-unique-character-in-a-string` |
| Topics | Hash Table, String, Queue, Counting |
| Solved | 2026-09-10 |
| Runtime | 55 ms (beats 77.66969999999998%) |
| Memory | 20.3 MB (beats 7.218000000000014%) |

## Problem Statement

Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

 

**Example 1:**

**Input:** s = "leetcode"

**Output:** 0

**Explanation:**

The character `'l'` at index 0 is the first character that does not occur at any other index.

**Example 2:**

**Input:** s = "loveleetcode"

**Output:** 2

**Example 3:**

**Input:** s = "aabb"

**Output:** -1

 

**Constraints:**

	- `1 <= s.length <= 105`

	- `s` consists of only lowercase English letters.

## Solutions

```Python3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s=list(s)
        d={}
        for v in s:
            d[v]=d.get(v,0)+1
        c=False

        for x in d:
            if d.get(x,0)==1:
                return s.index(x)
        return -1
```
