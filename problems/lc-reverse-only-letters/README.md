# Reverse Only Letters

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reverse-only-letters` |
| Topics | Two Pointers, String |
| Solved | 2026-06-17 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 36.967700000000015%) |

## Problem Statement

Given a string `s`, reverse the string according to the following rules:

	- All the characters that are not English letters remain in the same position.

	- All the English letters (lowercase or uppercase) should be reversed.

Return `s`_ after reversing it_.

 

**Example 1:**

**Input:** s = "ab-cd"
**Output:** "dc-ba"
**Example 2:**

**Input:** s = "a-bC-dEf-ghIj"
**Output:** "j-Ih-gfE-dCba"
**Example 3:**

**Input:** s = "Test1ng-Leet=code-Q!"
**Output:** "Qedo1ct-eeLg=ntse-T!"

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of characters with ASCII values in the range `[33, 122]`.

	- `s` does not contain `'\"'` or `'\\'`.

## Hints

<details>
<summary>Hint 1</summary>

This problem is exactly like reversing a normal string except that there are certain characters that we have to simply skip. That should be easy enough to do if you know how to reverse a string using the two-pointer approach.

</details>

## Solutions

```Python3
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        while i<j:
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i].isalpha():
                j-=1
            else:
                i+=1
        return "".join(s)
```
