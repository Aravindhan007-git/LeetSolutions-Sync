# Find All Anagrams in a String

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-find-all-anagrams-in-a-string` |
| Topics | Hash Table, String, Sliding Window |
| Solved | 2026-06-25 |
| Runtime | 23 ms (beats 96.58459999999998%) |
| Memory | 19.8 MB (beats 42.479%) |

## Problem Statement

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in **any order**.

 

**Example 1:**

**Input:** s = "cbaebabacd", p = "abc"
**Output:** [0,6]
**Explanation:**
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

**Example 2:**

**Input:** s = "abab", p = "ab"
**Output:** [0,1,2]
**Explanation:**
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

 

**Constraints:**

	- `1 <= s.length, p.length <= 3 * 104`

	- `s` and `p` consist of lowercase English letters.

## Solutions

```Python3
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sl=len(s)
        pl=len(p)
        if pl>sl:
            return []
        a=[0]*26
        b=[0]*26
        x=[]
        for i in p:
            b[ord(i)-ord('a')]+=1
        for i in range(sl):
            a[ord(s[i])-ord('a')]+=1
            if i>=pl:
                a[ord(s[i-pl])-ord('a')]-=1
            if i>=pl-1 and  a==b:
                x.append(i-pl+1)
        return x
```
