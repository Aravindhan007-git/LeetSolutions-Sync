# Reverse String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reverse-string` |
| Topics | Two Pointers, String |
| Solved | 2026-06-16 |
| Runtime | 0 ms (beats 100%) |
| Memory | 23.4 MB (beats 81.06660000000002%) |

## Problem Statement

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

 

**Example 1:**

**Input:** s = ["h","e","l","l","o"]
**Output:** ["o","l","l","e","h"]
**Example 2:**

**Input:** s = ["H","a","n","n","a","h"]
**Output:** ["h","a","n","n","a","H"]

 

**Constraints:**

	- `1 <= s.length <= 105`

	- `s[i]` is a printable ascii character.

## Hints

<details>
<summary>Hint 1</summary>

The entire logic for reversing a string is based on using the opposite directional two-pointer approach!

</details>

## Solutions

```Python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0
        j=len(s)-1
        while i<=j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
```
