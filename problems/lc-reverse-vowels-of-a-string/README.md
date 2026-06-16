# Reverse Vowels of a String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reverse-vowels-of-a-string` |
| Topics | Two Pointers, String |
| Solved | 2026-06-16 |
| Runtime | 15 ms (beats 31.7483%) |
| Memory | 20.5 MB (beats 51.83279999999999%) |

## Problem Statement

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

 

**Example 1:**

**Input:** s = "IceCreAm"

**Output:** "AceCreIm"

**Explanation:**

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

**Example 2:**

**Input:** s = "leetcode"

**Output:** "leotcede"

 

**Constraints:**

	- `1 <= s.length <= 3 * 105`

	- `s` consist of **printable ASCII** characters.

## Solutions

```Python3
class Solution:
    def reverseVowels(self, s: str) -> str:
        v=['A','E','I','O','U','a','e','i','o','u']
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if s[i] not in v:
                i+=1
                continue
            elif s[j] not in v:
                j-=1
                continue
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return "".join(s)

```
