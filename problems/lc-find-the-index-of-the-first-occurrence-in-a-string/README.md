# Find the Index of the First Occurrence in a String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-the-index-of-the-first-occurrence-in-a-string` |
| Topics | Two Pointers, String, String Matching, Z Algorithm, Knuth–morris–pratt Algorithm, Boyer–moore String Search Algorithm |
| Solved | 2026-04-30 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.1 MB (beats 91.528%) |

## Problem Statement

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

 

**Example 1:**

**Input:** haystack = "sadbutsad", needle = "sad"
**Output:** 0
**Explanation:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

**Example 2:**

**Input:** haystack = "leetcode", needle = "leeto"
**Output:** -1
**Explanation:** "leeto" did not occur in "leetcode", so we return -1.

 

**Constraints:**

	- `1 <= haystack.length, needle.length <= 104`

	- `haystack` and `needle` consist of only lowercase English characters.

## Solutions

```Python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
```
